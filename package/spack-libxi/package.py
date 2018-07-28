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


class Libxi(AutotoolsPackage):
    """libXi - library for the X Input Extension."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libXi"
    url      = "https://www.x.org/archive/individual/lib/libXi-1.7.6.tar.gz"

    version('1.7.6', 'f3828f9d7893068f6f6f10fe15b31afa')

    depends_on('pkgconfig', type='build')
    depends_on('libx11@1.6:')
    depends_on('libxext@1.0.99.1:')
    depends_on('libxfixes@5:')

    # transient build dependency (from libxfixes), i.e. shouldn't be needed?
    depends_on('fixesproto@5.0:', type='build')

    depends_on('xproto@7.0.13:', type='build')
    depends_on('xextproto@7.0.3:', type='build')
    depends_on('inputproto@2.2.99.1:', type='build')
