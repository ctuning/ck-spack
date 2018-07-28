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


class PyBrian2(PythonPackage):
    """A clock-driven simulator for spiking neural networks"""

    homepage = "http://www.briansimulator.org"
    url      = "https://pypi.io/packages/source/B/Brian2/Brian2-2.0.1.tar.gz"

    version('2.0.1', 'df5990e9a71f7344887bc02f54dfd0f0')
    version('2.0rc3', '3100c5e4eb9eb83a06ff0413a7d43152')

    variant('doc', default=False, description='Build the documentation')

    # depends on py-setuptools@6: for windows, if spack targets windows,
    # this will need to be added here
    depends_on('py-setuptools',     type='build')
    depends_on('py-numpy@1.8.2:',   type=('build', 'run'))
    depends_on('py-sympy@0.7.6:',   type=('build', 'run'))
    depends_on('py-pyparsing',      type=('build', 'run'))
    depends_on('py-jinja2@2.7:',    type=('build', 'run'))
    depends_on('py-cpuinfo@0.1.6:', type=('build', 'run'))
    depends_on('py-sphinx@1.4.2:',  type=('build', 'run'), when='+docs')
    depends_on('py-nosetests@1.0:', type='test')