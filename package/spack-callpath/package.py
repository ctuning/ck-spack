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


class Callpath(CMakePackage):
    """Library for representing callpaths consistently in
       distributed-memory performance tools."""

    homepage = "https://github.com/llnl/callpath"
    url      = "https://github.com/llnl/callpath/archive/v1.0.1.tar.gz"

    version('1.0.4', '39d2e06bfa316dec1085b874092e4b08')
    version('1.0.2', 'b1994d5ee7c7db9d27586fc2dcf8f373')
    version('1.0.1', '0047983d2a52c5c335f8ba7f5bab2325')

    depends_on('elf', type='link')
    depends_on('libdwarf')
    depends_on('dyninst')
    depends_on('adept-utils')
    depends_on('mpi')
    depends_on('cmake@2.8:', type='build')

    def cmake_args(self):
        # TODO: offer options for the walker used.
        args = ["-DCALLPATH_WALKER=dyninst"]

        if self.spec.satisfies("^dyninst@9.3.0:"):
            std_flag = self.compiler.cxx11_flag
            args.append("-DCMAKE_CXX_FLAGS='{0} -fpermissive'".format(
                std_flag))

        return args
