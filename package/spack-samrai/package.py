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


class Samrai(AutotoolsPackage):
    """SAMRAI (Structured Adaptive Mesh Refinement Application Infrastructure)
       is an object-oriented C++ software library enables exploration of
       numerical, algorithmic, parallel computing, and software issues
       associated with applying structured adaptive mesh refinement
       (SAMR) technology in large-scale parallel application development.

    """
    homepage = "https://computation.llnl.gov/projects/samrai"
    url      = "https://computation.llnl.gov/projects/samrai/download/SAMRAI-v3.11.2.tar.gz"
    list_url = homepage

    version('3.12.0',     '07364f6e209284e45ac0e9caf1d610f6')
    version('3.11.5',     '4359a03145c03501b230777f92b62104')
    version('3.11.4',     '473d6796772f5926b1c0d1cf8f3f8c99')
    # Version 3.11.3 permissions don't allow downloading
    version('3.11.2',     'd5f59f8efd755b23b797e46349428206')
    version('3.11.1',     '19a2398a7448ec0f0f0c5e8fc6f80478')
    version('3.10.0',     'ff5f5b8b4a35b52a1b7e37a74166c65a')
    version('3.9.1',      '232d04d0c995f5abf20d94350befd0b2')
    version('3.8.0',      'c18fcffa706346bfa5828b36787ce5fe')
    version('3.7.3',      '12d574eacadf8c9a70f1bb4cd1a69df6')
    version('3.7.2',      'f6a716f171c9fdbf3cb12f71fa6e2737')
    version('3.6.3-beta', 'ef0510bf2893042daedaca434e5ec6ce')
    version('3.5.2-beta', 'd072d9d681eeb9ada15ce91bea784274')
    version('3.5.0-beta', '1ad18a319fc573e12e2b1fbb6f6b0a19')
    version('3.4.1-beta', '00814cbee2cb76bf8302aff56bbb385b')
    version('3.3.3-beta', '1db3241d3e1cab913dc310d736c34388')
    version('3.3.2-beta', 'e598a085dab979498fcb6c110c4dd26c')
    version('2.4.4',      '04fb048ed0efe7c531ac10c81cc5f6ac')

    # Debug mode reduces optimization, includes assertions, debug symbols
    # and more print statements
    variant('debug', default=False,
            description='Compile with reduced optimization and debugging on')

    depends_on('mpi')
    depends_on('zlib')
    depends_on('hdf5+mpi')
    depends_on('m4', type='build')

    # Starting with 3.12.0, samrai no longer depends on boost.
    # version 3.11.5 or earlier can only work with boost version
    # 1.64.0 or earlier.
    depends_on('boost@:1.64.0', when='@0:3.11.99', type='build')

    # don't build tools with gcc
    patch('no-tool-build.patch', when='%gcc')

    def configure_args(self):
        options = []

        options.extend([
            '--with-CXX=%s' % self.spec['mpi'].mpicxx,
            '--with-CC=%s' % self.spec['mpi'].mpicc,
            '--with-F77=%s' % self.spec['mpi'].mpifc,
            '--with-M4=%s' % self.spec['m4'].prefix,
            '--with-hdf5=%s' % self.spec['hdf5'].prefix,
            '--with-zlib=%s' % self.spec['zlib'].prefix,
            '--without-blas',
            '--without-lapack',
            '--with-hypre=no',
            '--with-petsc=no'])

        if '+debug' in self.spec:
            options.extend([
                '--disable-opt',
                '--enable-debug'])
        else:
            options.extend([
                '--enable-opt',
                '--disable-debug'])

        if self.version >= Version('3.12.0'):
            # only version 3.12.0 and above, samrai does not use
            # boost, but needs c++11. Without c++11 flags, samrai
            # cannot build with either gcc or intel compilers.
            if 'CXXFLAGS' in env and env['CXXFLAGS']:
                env['CXXFLAGS'] += ' ' + self.compiler.cxx11_flag
            else:
                env['CXXFLAGS'] = self.compiler.cxx11_flag
        else:
            # boost 1.64.0 or earlier works with samrai 2.4.4~3.11.5
            options.append('--with-boost=%s' % self.spec['boost'].prefix)

        return options
