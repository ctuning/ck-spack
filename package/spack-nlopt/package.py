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


class Nlopt(CMakePackage):
    """NLopt is a free/open-source library for nonlinear optimization,
    providing a common interface for a number of different free optimization
    routines available online as well as original implementations of various
    other algorithms."""

    homepage = "https://nlopt.readthedocs.io"
    url      = "https://github.com/stevengj/nlopt/releases/download/nlopt-2.4.2/nlopt-2.4.2.tar.gz"

    version('develop', git='https://github.com/stevengj/nlopt.git', branch='master')
    version('2.4.2', 'd0b8f139a4acf29b76dbae69ade8ac54')

    variant('shared', default=True, description='Enables the build of shared libraries')
    variant('python', default=True, description='Build python wrappers')
    variant('guile',  default=False, description='Enable Guile support')
    variant('octave', default=False, description='Enable GNU Octave support')
    variant('cxx',    default=False,  description='Build the C++ routines')

    # Note: matlab is licenced - spack does not download automatically
    variant("matlab", default=False, description="Build the Matlab bindings.")

    depends_on('cmake@3.0:', type='build', when='@develop')
    depends_on('python', when='+python')
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    depends_on('swig', when='+python')
    depends_on('guile', when='+guile')
    depends_on('octave', when='+octave')
    depends_on('matlab', when='+matlab')

    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        spec = self.spec
        args = []

        # Specify on command line to alter defaults:
        # eg: spack install nlopt@develop +guile -octave +cxx

        # Spack should locate python by default - but to point to a build
        if '+python' in spec:
            args.append("-DPYTHON_EXECUTABLE=%s" % spec['python'].command.path)

        # On is default
        if '-shared' in spec:
            args.append('-DBUILD_SHARED_LIBS:Bool=OFF')

        if '+cxx' in spec:
            args.append('-DNLOPT_CXX:BOOL=ON')

        if '+matlab' in spec:
            args.append("-DMatlab_ROOT_DIR=%s" % spec['matlab'].command.path)

        return args
