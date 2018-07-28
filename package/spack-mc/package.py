##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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


class Mc(AutotoolsPackage):
    """The GNU Midnight Commander is a visual file manager."""

    homepage = "https://midnight-commander.org"
    url      = "http://ftp.midnight-commander.org/mc-4.8.20.tar.bz2"

    version('4.8.20', 'dcfc7aa613c62291a0f71f6b698d8267')

    depends_on('ncurses')
    depends_on('pkg-config', type='build')
    depends_on('glib@2.14:')
    depends_on('libssh2@1.2.5:')

    def setup_environment(self, spack_env, run_env):
        # Fix compilation bug on macOS by pretending we don't have utimensat()
        # https://github.com/MidnightCommander/mc/pull/130
        if 'darwin' in self.spec.architecture:
            env['ac_cv_func_utimensat'] = 'no'

    def configure_args(self):
        args = [
            '--disable-debug',
            '--disable-dependency-tracking',
            '--disable-silent-rules',
            '--without-x',
            '--with-screen=ncurses',
            '--enable-vfs-sftp'
        ]
        return args
