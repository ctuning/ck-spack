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


class PyUnittest2py3k(PythonPackage):
    """unittest2 is a backport of the new features added to the unittest
    testing framework in Python 2.7 and 3.2. This is a Python 3 compatible
    version of unittest2."""

    homepage = "https://pypi.python.org/pypi/unittest2py3k"
    url      = "https://pypi.io/packages/source/u/unittest2py3k/unittest2py3k-0.5.1.tar.gz"

    version('0.5.1', '8824ff92044310d9365f90d892bf0f09')

    depends_on('python@3:')
    depends_on('py-setuptools', type='build')
