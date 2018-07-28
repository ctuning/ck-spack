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


class Albany(CMakePackage):
    """Albany is an implicit, unstructured grid, finite element code for the
       solution and analysis of multiphysics problems.  The Albany repository
       on the GitHub site contains hundreds of regression tests and examples
       that demonstrate the code's capabilities on a wide variety of problems
       including fluid mechanics, solid mechanics (elasticity and plasticity),
       ice-sheet flow, quantum device modeling, and many other applications."""

    homepage = "http://gahansen.github.io/Albany"
    url      = "https://github.com/gahansen/Albany/tarball/master"

    maintainers = ['gahansen']

    version('develop', git='https://github.com/gahansen/Albany.git', branch='master')

    variant('lcm',          default=True,
            description='Enable LCM')
    variant('aeras',          default=False,
            description='Enable AERAS')
    variant('qcad',          default=False,
            description='Enable QCAD')
    variant('hydride',          default=False,
            description='Enable HYDRIDE')
    variant('lcm_spec',          default=False,
            description='Enable LCM_SPECULATIVE')
    variant('lame',          default=False,
            description='Enable LAME')
    variant('debug',          default=False,
            description='Enable DEBUGGING')
    variant('fpe',          default=False,
            description='Enable CHECK_FPE')
    variant('scorec',          default=False,
            description='Enable SCOREC')
    variant('felix',          default=False,
            description='Enable FELIX')
    variant('mor',          default=False,
            description='Enable MOR')
    variant('confgui',          default=False,
            description='Enable Albany configuration (CI) GUI')
    variant('ascr',          default=False,
            description='Enable ALBANY_ASCR')
    variant('perf',          default=False,
            description='Enable PERFORMANCE_TESTS')
    variant('64bit',          default=True,
            description='Enable 64BIT')

    # Add dependencies
    depends_on('mpi')
    depends_on('trilinos~superlu-dist+isorropia+tempus+rythmos+teko+intrepid+intrepid2+minitensor+phalanx+pnetcdf+nox+piro+rol+shards+stk+superlu@master,develop')

    def cmake_args(self):
        spec = self.spec
        trilinos_dir = spec['trilinos'].prefix
        options = []

        options.extend([
            '-DALBANY_TRILINOS_DIR:FILEPATH={0}'.format(trilinos_dir),
            '-DINSTALL_ALBANY:BOOL=ON'
        ])

        options.extend([
                       '-DENABLE_LCM:BOOL=%s' % (
                           'ON' if '+lcm' in spec else 'OFF'),
                       '-DENABLE_AERAS:BOOL=%s' % (
                           'ON' if '+aeras' in spec else 'OFF'),
                       '-DENABLE_QCAD:BOOL=%s' % (
                           'ON' if '+qcad' in spec else 'OFF'),
                       '-DENABLE_HYDRIDE:BOOL=%s' % (
                           'ON' if '+hydride' in spec else 'OFF'),
                       '-DENABLE_LCM_SPECULATIVE:BOOL=%s' % (
                           'ON' if '+lcm_spec' in spec else 'OFF'),
                       '-DENABLE_LAME:BOOL=%s' % (
                           'ON' if '+lame' in spec else 'OFF'),
                       '-DENABLE_DEBUGGING:BOOL=%s' % (
                           'ON' if '+debug' in spec else 'OFF'),
                       '-DENABLE_CHECK_FPE:BOOL=%s' % (
                           'ON' if '+fpe' in spec else 'OFF'),
                       '-DENABLE_SCOREC:BOOL=%s' % (
                           'ON' if '+scorec' in spec else 'OFF'),
                       '-DENABLE_FELIX:BOOL=%s' % (
                           'ON' if '+felix' in spec else 'OFF'),
                       '-DENABLE_MOR:BOOL=%s' % (
                           'ON' if '+mor' in spec else 'OFF'),
                       '-DENABLE_ALBANY_CI:BOOL=%s' % (
                           'ON' if '+ci' in spec else 'OFF'),
                       '-DENABLE_ASCR:BOOL=%s' % (
                           'ON' if '+ascr' in spec else 'OFF'),
                       '-DENABLE_PERFORMANCE_TESTS:BOOL=%s' % (
                           'ON' if '+perf' in spec else 'OFF'),
                       '-DENABLE_64BIT_INT:BOOL=%s' % (
                           'ON' if '+64bit' in spec else 'OFF')
                       ])

        return options
