##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
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


class Parsplice(CMakePackage):
    """ParSplice code implements the Parallel Trajectory Splicing algorithm"""

    homepage = "https://gitlab.com/exaalt/parsplice"
    url      = "https://gitlab.com/api/v4/projects/exaalt%2Fparsplice/repository/archive.tar.gz?sha=v1.1"

    tags = ['ecp', 'ecp-apps']

    version('1.1', '3a72340d49d731a076e8942f2ae2f4e9')
    version('develop', git='https://gitlab.com/exaalt/parsplice', branch='master')

    depends_on("cmake@3.1:", type='build')
    depends_on("berkeley-db")
    depends_on("nauty")
    depends_on("boost")
    depends_on("mpi")
    depends_on("eigen@3:")
    depends_on("lammps+lib@20170901:")

    def cmake_args(self):
        options = ['-DBUILD_SHARED_LIBS=ON']

        return options
