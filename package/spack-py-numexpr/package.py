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


class PyNumexpr(PythonPackage):
    """Fast numerical expression evaluator for NumPy"""
    homepage = "https://pypi.python.org/pypi/numexpr"
    url      = "https://pypi.io/packages/source/n/numexpr/numexpr-2.6.5.tar.gz"

    version('2.6.5', 'c9b5859c11bd6da092f6c8a84a472e77')
    version('2.6.1', '6365245705b446426df9543ad218dd8e')
    version('2.5',   '84f66cced45ba3e30dcf77a937763aaa')
    version('2.4.6', '17ac6fafc9ea1ce3eb970b9abccb4fbd')

    depends_on('python@2.6:')
    depends_on('py-numpy@1.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
