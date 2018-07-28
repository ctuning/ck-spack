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


class PyAstroid(PythonPackage):
    homepage = "https://www.astroid.org/"
    url      = "https://github.com/PyCQA/astroid/archive/astroid-1.4.5.tar.gz"

    # version('1.5.3', '6f65e4ea8290ec032320460905afb828') # has broken unit tests
    version('1.4.5', '7adfc55809908297ef430efe4ea20ac3')
    version('1.4.4', '8ae6f63f6a2b260bb7f647dafccbc796')
    version('1.4.3', '4647159de7d4d0c4b1de23ecbfb8e246')
    version('1.4.2', '677f7965840f375af51b0e86403bee6a')
    version('1.4.1', 'ed70bfed5e4b25be4292e7fe72da2c02')

    depends_on('py-lazy-object-proxy')
    depends_on('py-six')
    depends_on('py-wrapt')
    depends_on('py-enum34@1.1.3:', when='^python@:3.3.99')
    depends_on('py-singledispatch', when='^python@:3.3.99')
    depends_on('py-backports-functools-lru-cache', when='^python@:3.2.99')
    depends_on('py-setuptools@17.1:')
