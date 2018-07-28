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


class Tabix(MakefilePackage):
    """Generic indexer for TAB-delimited genome position files"""

    homepage = "https://github.com/samtools/tabix"
    url      = "https://github.com/samtools/tabix"

    version('2013-12-16', git='https://github.com/samtools/tabix.git', commit='1ae158ac79b459f5feeed7490c67519b14ce9f35')

    depends_on('perl', type=('build', 'run'))
    depends_on('python', type=('build', 'run'))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.share.man.man1)
        install('tabix', prefix.bin)
        install('bgzip', prefix.bin)
        install('tabix.py', prefix.bin)
        install('tabix.1', prefix.share.man.man1)
        install('tabix.tex', prefix.share)
        install('TabixReader.java', prefix.bin)
        install('libtabix.a', prefix.lib)
        install_tree('perl', prefix.perl)
        install_tree('python', prefix.python)
