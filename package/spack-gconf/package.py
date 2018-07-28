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


class Gconf(AutotoolsPackage):
    """GConf is a system for storing application preferences."""

    homepage = "https://projects.gnome.org/gconf/"
    url      = "http://ftp.gnome.org/pub/gnome/sources/GConf/3.2/GConf-3.2.6.tar.xz"

    version('3.2.6', '2b16996d0e4b112856ee5c59130e822c')

    depends_on('glib@2.14.0:')
    depends_on('libxml2')

    # TODO: add missing dependencies
    # gio-2.0 >= 2.31.0
    # gthread-2.0
    # gmodule-2.0 >= 2.7.0
    # gobject-2.0 >= 2.7.0
    # dbus-1 >= 1.0.0
    # dbus-glib-1 >= 0.74
