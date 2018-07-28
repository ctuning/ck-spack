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


class PyLazyarray(PythonPackage):
    """a Python package that provides a lazily-evaluated numerical array class,
    larray, based on and compatible with NumPy arrays."""

    homepage = "http://bitbucket.org/apdavison/lazyarray/"
    url      = "https://pypi.io/packages/source/l/lazyarray/lazyarray-0.2.8.tar.gz"

    version('0.2.10', '336033357459e66cbca5543bf003a2ba')
    version('0.2.8',  '8e0072f0892b9fc0516e7048f96e9d74')

    depends_on('py-numpy@1.3:', type=('build', 'run'))
    depends_on('py-numpy@1.5:', type=('build', 'run'), when='^python@3:')
