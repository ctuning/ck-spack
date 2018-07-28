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


class UtilLinux(AutotoolsPackage):
    """Util-linux is a suite of essential utilities for any Linux system."""

    homepage = "http://freecode.com/projects/util-linux"
    url      = "https://www.kernel.org/pub/linux/utils/util-linux/v2.29/util-linux-2.29.2.tar.gz"
    list_url = "https://www.kernel.org/pub/linux/utils/util-linux"
    list_depth = 1

    version('2.29.2', '24e0c67aac6f5c2535208866a42aeea2')
    version('2.29.1', 'c7d5c111ef6bc5df65659e0b523ac9d9')
    version('2.25',   'f6d7fc6952ec69c4dc62c8d7c59c1d57')

    depends_on('python@2.7:')

    def url_for_version(self, version):
        url = "https://www.kernel.org/pub/linux/utils/util-linux/v{0}/util-linux-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def configure_args(self):
        spec = self.spec

        return [
            'PKG_CONFIG_PATH={0}'.format(
                join_path(spec['python'].prefix.lib, 'pkgconfig')),
            '--disable-use-tty-group',
        ]
