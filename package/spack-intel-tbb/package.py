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
import glob
import inspect
import platform


class IntelTbb(Package):
    """Widely used C++ template library for task parallelism.
    Intel Threading Building Blocks (Intel TBB) lets you easily write parallel
    C++ programs that take full advantage of multicore performance, that are
    portable and composable, and that have future-proof scalability.
    """
    homepage = "http://www.threadingbuildingblocks.org/"

    # See url_for_version() below.
    version('2018.4', '5e2e6ba0e25624a94331c945856551c2')
    version('2018.3', 'cd2e136598ffa5c136f077ee85a35b4c')
    version('2018.2', '0b8dfe30917a54e40828eeb0ed7562ae')
    version('2018.1', 'b2f2fa09adf44a22f4024049907f774b')
    version('2018',   '7fb30d5ea2545f26ce02757d9ab05e6c')
    version('2017.8', '7240f57f1aeea0e266a5e17ae68fdc16')
    version('2017.7', '364f2a4b80e978f38a69cbf7c466b898')
    version('2017.6', 'ec21254af4fc2a29574c272f501a3138')
    version('2017.5', '85b41c64102c052e24d8a39f6193e599')
    version('2017.4', '71526b2fef098515e212302d1455de7d')
    version('2017.3', 'd7622eeaafeff8d271c7aa684bd82ddb')
    version('2017.2', '9605cbea96998a10a186fc72c35cbd76')
    version('2017.1', '6c0fe8aa7bc911a85e8e522e620511b3')
    version('2017',   '9e7f9ea684ecf84ac74dcd3c6012cfa6')
    version('4.4.6',  '20e15206f70c2651bfc964e451a443a0')
    version('4.4.5',  '531a67cd98f9b4ec8ece95c5f8193a83')
    version('4.4.4',  '61531b2e8684e06a621dcdca1a7a420e')
    version('4.4.3',  '8e3e39e1fdfb3f7c3a5ac8ec1afe186e')
    version('4.4.2',  'e92b110e8eb238741b00e3789b39969e')
    version('4.4.1',  'a02c9958f02c1b5f3626874219979ae8')
    version('4.4',    '1d512085221996eae6cec04e1a4cd3dd')

    provides('tbb')

    conflicts('%gcc@6.1:', when='@:4.4.3',
              msg='4.4.4 or later required for GCC >= 6.1.')

    variant('shared', default=True,
            description='Builds a shared version of TBB libraries')

    variant('cxxstd',
            default='default',
            values=('default', '98', '11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    # Build and install CMake config files if we're new enough.
    depends_on('cmake@3.0.0:', type='build', when='@2017.0:')

    # Deactivate use of RTM with GCC when on an OS with an elderly assembler.
    patch("tbb_gcc_rtm_key.patch", level=0, when='%gcc@4.8.0: os=rhel6')
    patch("tbb_gcc_rtm_key.patch", level=0, when='%gcc@4.8.0: os=scientific6')
    patch("tbb_gcc_rtm_key.patch", level=0, when='%gcc@4.8.0: os=centos6')

    # Patch cmakeConfig.cmake.in to find the libraries where we install them.
    patch("tbb_cmakeConfig.patch", level=0, when='@2017.0:')

    def url_for_version(self, version):
        url = 'https://github.com/01org/tbb/archive/{0}.tar.gz'
        if (version[0] >= 2017) and len(version) > 1:
            return url.format('{0}_U{1}'.format(version[0], version[1]))
        else:
            return url.format(version)

    def coerce_to_spack(self, tbb_build_subdir):
        for compiler in ["icc", "gcc", "clang"]:
            fs = glob.glob(join_path(tbb_build_subdir,
                                     "*.%s.inc" % compiler))
            for f in fs:
                lines = open(f).readlines()
                of = open(f, "w")
                for l in lines:
                    if l.strip().startswith("CPLUS ="):
                        of.write("# coerced to spack\n")
                        of.write("CPLUS = $(CXX)\n")
                    elif l.strip().startswith("CPLUS ="):
                        of.write("# coerced to spack\n")
                        of.write("CONLY = $(CC)\n")
                    else:
                        of.write(l)

    def install(self, spec, prefix):
        # We need to follow TBB's compiler selection logic to get the proper
        # build + link flags but we still need to use spack's compiler wrappers
        # to accomplish this, we do two things:
        #
        # * Look at the spack spec to determine which compiler we should pass
        #   to tbb's Makefile;
        #
        # * patch tbb's build system to use the compiler wrappers (CC, CXX) for
        #   icc, gcc, clang (see coerce_to_spack());
        #
        self.coerce_to_spack("build")

        if spec.satisfies('%clang'):
            tbb_compiler = "clang"
        elif spec.satisfies('%intel'):
            tbb_compiler = "icc"
        else:
            tbb_compiler = "gcc"

        mkdirp(prefix)
        mkdirp(prefix.lib)

        make_opts = []

        # Static builds of TBB are enabled by including 'big_iron.inc' file
        # See caveats in 'big_iron.inc' for limits on using TBB statically
        # Lore states this file must be handed to make before other options
        if '+shared' not in self.spec:
            make_opts.append("extra_inc=big_iron.inc")

        if spec.variants['cxxstd'].value != 'default':
            make_opts.append('stdver=c++{0}'.
                             format(spec.variants['cxxstd'].value))

        #
        # tbb does not have a configure script or make install target
        # we simply call make, and try to put the pieces together
        #
        make_opts.append("compiler={0}".format(tbb_compiler))
        make(*make_opts)

        # install headers to {prefix}/include
        install_tree('include', prefix.include)

        # install libs to {prefix}/lib
        tbb_lib_names = ["libtbb",
                         "libtbbmalloc",
                         "libtbbmalloc_proxy"]

        for lib_name in tbb_lib_names:
            # install release libs
            fs = glob.glob(join_path("build", "*release", lib_name + ".*"))
            for f in fs:
                install(f, prefix.lib)
            # install debug libs if they exist
            fs = glob.glob(join_path("build", "*debug", lib_name + "_debug.*"))
            for f in fs:
                install(f, prefix.lib)

        if self.spec.satisfies('@2017.0:'):
            # Generate and install the CMake Config file.
            cmake_args = ('-DTBB_ROOT={0}'.format(prefix),
                          '-DTBB_OS={0}'.format(platform.system()),
                          '-P',
                          'tbb_config_generator.cmake')
            with working_dir(join_path(self.stage.source_path, 'cmake')):
                inspect.getmodule(self).cmake(*cmake_args)
