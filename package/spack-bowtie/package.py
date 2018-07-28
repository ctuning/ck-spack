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


class Bowtie(MakefilePackage):
    """Bowtie is an ultrafast, memory-efficient short read aligner
    for short DNA sequences (reads) from next-gen sequencers."""

    homepage = "https://sourceforge.net/projects/bowtie-bio/"
    url      = "https://downloads.sourceforge.net/project/bowtie-bio/bowtie/1.2.0/bowtie-1.2-source.zip"

    version('1.2', '6d97f0ea1a65af11d17cc270cfac4af9')

    variant('tbb', default=False, description='Use Intel thread building block')

    depends_on('tbb', when='+tbb')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter('CC = .*', 'CC = ' + env['CC'])
        makefile.filter('CXX = .*', 'CPP = ' + env['CXX'])

    def build(self, spec, prefix):
        if '+tbb' in spec:
            make()
        else:
            make('NO_TBB=1')

    def install(self, spec, prefix):
        make('prefix={0}'.format(self.prefix), 'install')
