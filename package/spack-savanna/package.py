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
from distutils.dir_util import copy_tree


class Savanna(MakefilePackage):
    """CODARcode Savanna runtime framework for high performance,
    workflow management using Swift/T and ADIOS.
    """

    homepage = "https://github.com/CODARcode/savanna"
    url = "https://github.com/CODARcode/savanna/archive/v0.5.tar.gz"

    version('develop', git='https://github.com/CODARcode/savanna.git',
            branch='master', submodules=True)
    version('0.5', git='https://github.com/CODARcode/savanna.git',
            tag='0.5', submodules=True)

    variant('tau', default=False, description='Enable TAU profiling support')

    depends_on('mpi')
    depends_on('stc')
    depends_on('adios +fortran +zlib +sz +zfp +staging')
    depends_on('mpix-launch-swift')
    depends_on('tau', when='+tau')

    def install(self, spec, prefix):
        copy_tree('.', prefix)
