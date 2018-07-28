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


class Gccxml(CMakePackage):
    """gccxml dumps an XML description of C++ source code using an extension of
    the GCC C++ compiler."""

    homepage = "http://gccxml.github.io"
    url      = "https://github.com/gccxml/gccxml/archive/v0.6.x.tar.gz"

    version('develop', git='https://github.com/gccxml/gccxml.git', branch='master')
    version('latest', git='https://github.com/gccxml/gccxml.git',
            commit='3afa8ba5be6866e603dcabe80aff79856b558e24', preferred=True)

    patch('darwin-gcc.patch', when='%gcc platform=darwin')
    # taken from https://github.com/gccxml/gccxml/issues/11#issuecomment-140334118
    patch('gcc-5.patch', when='%gcc@5:')
