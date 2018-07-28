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
from shutil import copyfile
from shutil import copymode


class Bioawk(MakefilePackage):
    """Bioawk is an extension to Brian Kernighan's awk, adding the support of
       several common biological data formats, including optionally gzip'ed
       BED, GFF, SAM, VCF, FASTA/Q and TAB-delimited formats with column names.
    """

    homepage = "https://github.com/lh3/bioawk"
    url = "https://github.com/lh3/bioawk/archive/v1.0.zip"

    version('1.0', 'e423942689f944369de270900978be28')

    depends_on('zlib')
    depends_on('bison', type=('build'))

    parallel = False

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        copyfile("bioawk", join_path(prefix.bin, "bioawk"))
        copymode("bioawk", join_path(prefix.bin, "bioawk"))
        copyfile("maketab", join_path(prefix.bin, "maketab"))
        copymode("maketab", join_path(prefix.bin, "maketab"))
