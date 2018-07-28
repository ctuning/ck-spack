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


class Libxpm(AutotoolsPackage):
    """libXpm - X Pixmap (XPM) image file format library."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libXpm"
    url      = "https://www.x.org/archive//individual/lib/libXpm-3.5.12.tar.gz"

    version('3.5.12', 'b286c884b11b5a0b4371175c5327141f')
    version('3.5.11', '7c67c878ee048206b070bc0b24154f04')
    version('3.5.10', 'a70507638d74541bf30a771f1e5938bb')
    version('3.5.9', 'd6d4b0f76248a6b346eb42dfcdaa72a6')
    version('3.5.8', '2d81d6633e67ac5562e2fbee126b2897')
    version('3.5.7', '7bbc8f112f7143ed6961a58ce4e14558')

    depends_on('gettext')
    depends_on('libx11')

    depends_on('xproto', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    def setup_environment(self, spack_env, run_env):
        spack_env.append_flags('LDFLAGS', '-L{0} -lintl'.format(
            self.spec['gettext'].prefix.lib))
