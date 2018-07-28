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


class XtensorPython(CMakePackage):
    """Python bindings for the xtensor C++ multi-dimensional array library"""

    homepage = "https://xtensor-python.readthedocs.io"
    url      = "https://github.com/QuantStack/xtensor-python/archive/0.17.0.tar.gz"
    maintainers = ['ax3l']

    version('develop', branch='master',
            git='https://github.com/QuantStack/xtensor-python.git')
    version('0.17.0', '51d22e42909a81201c3421d9e119eed0')

    depends_on('xtensor@0.15.1:0.15.99', when='@0.17.0:')
    depends_on('xtl@0.4.0:0.4.99', when='@0.17.0:')
    depends_on('py-pybind11@2.2.1', when='@0.17.0:')

    depends_on('py-numpy')
    depends_on('python', type=('build', 'link', 'run'))

    extends('python')

    def cmake_args(self):
        spec = self.spec

        python_exe = spec['python'].command.path

        args = [
            '-DPYTHON_EXECUTABLE={0}'.format(python_exe)
        ]
        return args
