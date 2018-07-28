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


class Pflotran(AutotoolsPackage):
    """PFLOTRAN is an open source, state-of-the-art massively parallel
       subsurface flow and reactive transport code.
    """

    homepage = "http://www.pflotran.org"

    version('develop', git='https://bitbucket.org/pflotran/pflotran')
    version('xsdk-0.2.0', git='https://bitbucket.org/pflotran/pflotran', tag='master')
    version('xsdk-0.3.0', git='https://bitbucket.org/pflotran/pflotran', branch='release/xsdk-0.3.0')

    depends_on('mpi')
    depends_on('hdf5@1.8.12:+mpi+fortran')
    depends_on('petsc@develop+hdf5+metis', when='@develop')
    depends_on('petsc@xsdk-0.2.0+hdf5+metis', when='@xsdk-0.2.0')    
    depends_on('petsc@3.8.0:+hdf5+metis', when='@xsdk-0.3.0')

    parallel = False
