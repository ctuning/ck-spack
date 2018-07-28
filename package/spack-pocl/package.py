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
import os

from spack import *
from spack.package_test import compile_c_and_execute, compare_output_file


class Pocl(CMakePackage):
    """Portable Computing Language (pocl) is an open source implementation
    of the OpenCL standard which can be easily adapted for new targets
    and devices, both for homogeneous CPU and heterogeneous
    GPUs/accelerators."""

    homepage = "http://portablecl.org"
    url = "http://portablecl.org/downloads/pocl-0.13.tar.gz"

    version("master", git="https://github.com/pocl/pocl.git")
    version('0.14', '1d35f09299e76b9e3918c42826555194')
    # version("0.14-rc",
    #         git="https://github.com/pocl/pocl.git", branch="release_0_14")
    version("0.13", "344480864d4269f2f63f1509395898bd")
    version("0.12", "e197ba3aa01a35f40581c48e053330dd")
    version("0.11", "9be0640cde2983062c47393d9e8e8fe7")
    version("0.10", "0096be4f595c7b5cbfa42430c8b3af6a")

    # This is Github's pocl/pocl#373
    patch("uint.patch", when="@:0.13")
    patch("vecmathlib.patch", when="@:0.13")

    # Note: We should describe correctly which pocl versions provide
    # which version of the  OpenCL standard
    # OpenCL standard versions are: 1.0, 1.1, 1.2, 2.0, 2.1, 2.2
    provides('opencl@:2.0')

    depends_on("cmake @2.8.12:", type="build")
    depends_on("hwloc")
    depends_on("libtool", type=("build", "link", "run"))
    depends_on("pkgconfig", type="build")

    # We don't request LLVM's shared libraries because these are not
    # enabled by default, and also because they fail to build for us
    # (see #1616)
    # These are the supported LLVM versions
    depends_on("llvm +clang @3.7:3.9", when="@master")
    depends_on("llvm +clang @3.7:4.0", when="@0.14")
    depends_on("llvm +clang @3.7:3.8", when="@0.13")
    depends_on("llvm +clang @3.2:3.7", when="@0.12")
    depends_on("llvm +clang @3.2:3.6", when="@0.11")
    depends_on("llvm +clang @3.2:3.5", when="@0.10")

    variant("distro", default=False,
            description=("Support several CPU architectures, "
                         "suitable e.g. in a build "
                         "that will be made available for download"))
    variant("icd", default=False,
            description="Support a system-wide ICD loader")

    def cmake_args(self):
        spec = self.spec
        args = ["-DINSTALL_OPENCL_HEADERS=ON"]
        if "~shared" in spec["llvm"]:
            args += ["-DSTATIC_LLVM"]
        if "+distro" in spec:
            args += ["-DKERNELLIB_HOST_CPU_VARIANTS=distro"]
        args += ["-DENABLE_ICD=%s" % ("ON" if "+icd" in spec else "OFF")]
        return args

    @run_after('install')
    def symlink_opencl(self):
        os.symlink("CL", self.prefix.include.OpenCL)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def check_install(self):
        # Build and run a small program to test the installed OpenCL library
        spec = self.spec
        print("Checking pocl installation...")
        checkdir = "spack-check"
        with working_dir(checkdir, create=True):
            source = join_path(os.path.dirname(self.module.__file__),
                               "example1.c")
            cflags = spec["pocl"].headers.cpp_flags.split()
            # ldflags = spec["pocl"].libs.ld_flags.split()
            ldflags = ["-L%s" % spec["pocl"].prefix.lib,
                       "-lOpenCL", "-lpoclu"]
            output = compile_c_and_execute(source, cflags, ldflags)
            compare_output_file(
                output,
                join_path(os.path.dirname(self.module.__file__),
                          "example1.out"))
