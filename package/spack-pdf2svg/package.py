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


class Pdf2svg(AutotoolsPackage):
    """A simple PDF to SVG converter using the Poppler and Cairo libraries."""

    homepage = "http://www.cityinthesky.co.uk/opensource/pdf2svg"
    url      = "https://github.com/dawbarton/pdf2svg/archive/v0.2.3.tar.gz"

    version('0.2.3', 'd398b3b1c1979f554596238a44f12123')
    version('0.2.2', 'f7e0d2213f9e1422cee9421e18f72553')

    depends_on('cairo', type='run')
    depends_on('poppler', type='run')
