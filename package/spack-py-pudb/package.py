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


class PyPudb(PythonPackage):
    """Full-screen console debugger for Python"""

    homepage = "http://mathema.tician.de/software/pudb"
    url      = "https://pypi.io/packages/source/p/pudb/pudb-2017.1.1.tar.gz"

    version('2017.1.1', '4ec3302ef90f22b13c60db16b3557c56')
    version('2016.2',   '4573b70163329c1cb59836a357bfdf7c')

    # Most Python packages only require setuptools as a build dependency.
    # However, pudb requires setuptools during runtime as well.
    depends_on('py-setuptools',    type=('build', 'run'))
    depends_on('py-urwid@1.1.1:',  type=('build', 'run'))
    depends_on('py-pygments@1.0:', type=('build', 'run'))
