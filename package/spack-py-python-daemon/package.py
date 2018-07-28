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


class PyPythonDaemon(PythonPackage):
    """Library to implement a well-behaved Unix daemon process.

       This library implements the well-behaved daemon specification of
       PEP Standard daemon process.

       A well-behaved Unix daemon process is tricky to get right, but the
       required steps are much the same for every daemon program. A
       DaemonContext instance holds the behaviour and configured process
       environment for the program; use the instance as a context manager
       to enter a daemon state.
    """
    homepage = "https://pypi.python.org/pypi/python-daemon/"
    url      = "https://pypi.io/packages/source/p/python-daemon/python-daemon-2.0.5.tar.gz"

    version('2.0.5', '73e7f49f525c51fa4a995aea4d80de41')

    depends_on("py-setuptools", type='build')
    depends_on("py-lockfile", type=('build', 'run'))
