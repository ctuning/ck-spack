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


class Libjpeg(AutotoolsPackage):
    """libjpeg is a widely used free library with functions for handling the
    JPEG image data format. It implements a JPEG codec (encoding and decoding)
    alongside various utilities for handling JPEG data."""

    homepage = "http://www.ijg.org"
    url      = "http://www.ijg.org/files/jpegsrc.v9c.tar.gz"

    version('9c', '93c62597eeef81a84d988bccbda1e990')
    version('9b', '6a9996ce116ec5c52b4870dbcd6d3ddb')
    version('9a', '3353992aecaee1805ef4109aadd433e7')

    provides('jpeg')

    def check(self):
        # Libjpeg has both 'check' and 'test' targets that are aliases.
        # Only need to run the tests once.
        make('check')
