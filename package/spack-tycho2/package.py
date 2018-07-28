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


class Tycho2(MakefilePackage):
    """A neutral particle transport mini-app to study performance of sweeps
       on unstructured, 3D tetrahedral meshes.
    """
    homepage = "https://github.com/lanl/tycho2"
    url      = "https://github.com/lanl/tycho2/tarball/v0.1"

    version('develop', git='https://github.com/lanl/tycho2', branch='master')

    depends_on("mpi")

    def patch(self):
        # make.inc is included by Makefile to set MPICC, but we that
        # through build_targets() below, so any empty include file is fine.
        touch('make.inc')

    @property
    def build_targets(self):
        targets = [
            'MPICC={0} -std=c++11 {1}'.format(self.spec['mpi'].mpicxx,
                                              self.compiler.openmp_flag)
        ]

        return targets

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('sweep.x', prefix.bin)
