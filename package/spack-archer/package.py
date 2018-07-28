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


class Archer(CMakePackage):
    """ARCHER, a data race detection tool for large OpenMP applications."""

    homepage = "https://github.com/PRUNERS/ARCHER"
    url      = "https://github.com/PRUNERS/archer/archive/v1.0.0.tar.gz"

    version('1.0.0', '790bfaf00b9f57490eb609ecabfe954a')

    depends_on('cmake@3.4.3:', type='build')
    depends_on('llvm')
    depends_on('ninja@1.5:', type='build')
    depends_on('llvm-openmp-ompt')

    generator = 'Ninja'

    def cmake_args(self):
        return [
            '-DCMAKE_C_COMPILER=clang',
            '-DCMAKE_CXX_COMPILER=clang++',
            '-DOMP_PREFIX:PATH=%s' % self.spec['llvm-openmp-ompt'].prefix,
        ]
