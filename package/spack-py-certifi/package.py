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


class PyCertifi(PythonPackage):
    """Certifi: A carefully curated collection of Root Certificates for validating
    the trustworthiness of SSL certificates while verifying the identity of TLS
    hosts."""
    homepage = "http://certifi.io/"
    url      = "https://pypi.io/packages/source/c/certifi/certifi-2017.1.23.tar.gz"

    import_modules = ['certifi']

    version('2017.1.23',  'b72521a8badff5e89a8eabea586d79ab')
    version('2016.02.28', '5ccfc23bd5e931863f0b01ef3e9d2dbd3bef0e1b')

    depends_on('py-setuptools', type='build')