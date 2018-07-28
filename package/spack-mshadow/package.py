##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the LICENSE file for our notice and the LGPL.
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


class Mshadow(Package):
    """MShadow is a lightweight CPU/GPU Matrix/Tensor C++ Template Library.
    in C++/CUDA."""

    homepage = "https://github.com/dmlc/mshadow"
    url      = "https://github.com/dmlc/mshadow/archive/v1.1.tar.gz"

    version('master', git='https://github.com/dmlc/mshadow.git', branch='master')
    version('20170721', git='https://github.com/dmlc/mshadow.git',
            commit='20b54f068c1035f0319fa5e5bbfb129c450a5256')

    def install(self, spec, prefix):
        install_tree('mshadow', prefix.include.mshadow)
        install_tree('make', prefix.make)
