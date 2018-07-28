##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Scalpel(MakefilePackage):
    """Scalpel is a software package for detecting INDELs (INsertions and
       DELetions) mutations in a reference genome which has been sequenced
       with next-generation sequencing technology.
    """

    homepage = "http://scalpel.sourceforge.net/index.html"
    url      = "https://downloads.sourceforge.net/project/scalpel/scalpel-0.5.3.tar.gz"

    version('0.5.3', '682c9f1cd6ab2cb11c6866f303c673f0')

    depends_on('cmake')
    depends_on('perl@5.10.0:')

    # bamtools needs to build before the others.
    parallel = False

    @run_before('install')
    def filter_sbang(self):
        """Run before install so that the standard Spack sbang install hook
        can fix up the path to the perl|python binary.
        """

        with working_dir(self.stage.source_path):
            kwargs = {'ignore_absent': True, 'backup': False, 'string': False}

            match = '^#!/usr/bin/env perl'
            perl = self.spec['perl'].command
            substitute = "#!{perl}".format(perl=perl)
            files = ['FindDenovos.pl', 'scalpel-export',
                     'scalpel-discovery', 'FindVariants.pl',
                     'FindSomatic.pl']
            filter_file(match, substitute, *files, **kwargs)

    # Scalpel doesn't actually *have* an install step.  The authors
    # expect you to unpack the tarball, build it in the resulting
    # directory, and add that directory to your PATH.  The Perl
    # scripts use `FindBin` to discover the directory in which they
    # live and they run their own dedicated copies of {bam,sam}tools
    # and etc... by explicitly naming the executables in their directory.
    #
    # Rather than trying to fix their code I just copied the juicy
    # bits into prefix.bin. It's not normal, but....
    #
    def install(self, spec, prefix):
        destdir = prefix.bin    # see the note above....

        mkdirp(destdir)

        files = ['FindSomatic.pl', 'HashesIO.pm', 'MLDBM.pm',
                 'scalpel-export', 'Utils.pm', 'FindDenovos.pl',
                 'FindVariants.pl', 'scalpel-discovery',
                 'SequenceIO.pm', 'Usage.pm']
        for f in files:
            install(f, destdir)

        dirs = ['Text',  'MLDBM', 'Parallel', ]
        for d in dirs:
            install_tree(d, join_path(destdir, d))

        install_tree('bamtools-2.3.0/bin',
                     join_path(destdir, 'bamtools-2.3.0', 'bin'))
        install_tree('bamtools-2.3.0/lib',
                     join_path(destdir, 'bamtools-2.3.0', 'lib'))

        mkdirp(join_path(destdir, 'bcftools-1.1'))
        install('bcftools-1.1/bcftools', join_path(destdir, 'bcftools-1.1'))

        mkdirp(join_path(destdir, 'Microassembler'))
        install('Microassembler/Microassembler',
                join_path(destdir, 'Microassembler'))

        mkdirp(join_path(destdir, 'samtools-1.1'))
        install('samtools-1.1/samtools', join_path(destdir, 'samtools-1.1'))
