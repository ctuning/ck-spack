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


class Fixesproto(AutotoolsPackage):
    """X Fixes Extension.

    The extension makes changes to many areas of the protocol to resolve
    issues raised by application interaction with core protocol mechanisms
    that cannot be adequately worked around on the client side of the wire."""

    homepage = "http://cgit.freedesktop.org/xorg/proto/fixesproto"
    url      = "https://www.x.org/archive/individual/proto/fixesproto-5.0.tar.gz"

    version('5.0', '1b3115574cadd4cbea1f197faa7c1de4')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
