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


class PyGenshi(PythonPackage):
    """Python toolkit for generation of output for the web"""
    homepage = "https://genshi.edgewall.org/"
    url      = "http://ftp.edgewall.com/pub/genshi/Genshi-0.7.tar.gz"

    version('0.7', '54e64dd69da3ec961f86e686e0848a82')
    version('0.6.1', '372c368c8931110b0a521fa6091742d7')
    version('0.6', '604e8b23b4697655d36a69c2d8ef7187')

    depends_on("py-setuptools", type='build')
