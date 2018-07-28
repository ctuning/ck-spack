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


class PyYt(PythonPackage):
    """Volumetric Data Analysis

       yt is a python package for analyzing and visualizing
       volumetric, multi-resolution data from astrophysical
       simulations, radio telescopes, and a burgeoning
       interdisciplinary community.
    """
    homepage = "http://yt-project.org"
    url = "https://github.com/yt-project/yt.git"

    version("3.4.0", "413b835f1b0e2a0bd26f1044ff7dbc94",
            url="https://github.com/yt-project/yt/archive/yt-3.4.0.tar.gz")
    version("3.3.5", "2ad314ff3d3261e41825d15db027b0e7",
            url="https://bitbucket.org/yt_analysis/yt/get/yt-3.3.5.tar.gz")
    version("3.3.4", "3a84e56dfd82f9dd923f3fb8490e679c",
            url="https://bitbucket.org/yt_analysis/yt/get/yt-3.3.4.tar.gz")
    version("3.3.1", hg="https://bitbucket.org/yt_analysis/yt",
            tag="yt-3.3.1", commit="9bc3d0e9b750c923d44d73c447df64fc431f5838")
    version("3.2.3", hg="https://bitbucket.org/yt_analysis/yt",
            tag="yt-3.2.3", commit="83d2c1e9313e7d83eb5b96888451ff2646fd8ff3")
    version("3.1.0", hg="https://bitbucket.org/yt_analysis/yt",
            tag="yt-3.1.0", commit="fd7cdc4836188a3badf81adb477bcc1b9632e485")
    version("3.0.2", hg="https://bitbucket.org/yt_analysis/yt",
            tag="yt-3.0.2", commit="511887af4c995a78fe606e58ce8162c88380ecdc")
    version("2.6.3", hg="https://bitbucket.org/yt_analysis/yt",
            tag="yt-2.6.3", commit="816186f16396a16853810ac9ebcde5057d8d5b1a")
    version("develop", git="https://github.com/yt-project/yt.git",
            branch="master")

    variant("astropy", default=True, description="enable astropy support")
    variant("h5py", default=True, description="enable h5py support")
    variant("scipy", default=True, description="enable scipy support")
    variant("rockstar", default=False, description="enable rockstar support")

    depends_on("py-astropy", type=('build', 'run'), when="+astropy")
    depends_on("py-cython", type=('build', 'run'))
    depends_on("py-h5py", type=('build', 'run'), when="+h5py")
    depends_on("py-ipython", type=('build', 'run'))
    depends_on("py-matplotlib", type=('build', 'run'))
    depends_on("py-numpy", type=('build', 'run'))
    depends_on("py-scipy", type=('build', 'run'), when="+scipy")
    depends_on("py-setuptools", type=('build', 'run'))
    depends_on("py-sympy", type=('build', 'run'))
    depends_on("rockstar@yt", type=('build', 'run'), when="+rockstar")
    depends_on("python@2.7:2.8,3.4:")

    @run_before('install')
    def prep_yt(self):
        if '+rockstar' in self.spec:
            with open('rockstar.cfg', 'w') as rockstar_cfg:
                rockstar_cfg.write(self.spec['rockstar'].prefix)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def check_install(self):
        # The Python interpreter path can be too long for this
        # yt = Executable(join_path(prefix.bin, "yt"))
        # yt("--help")
        python(join_path(self.prefix.bin, "yt"), "--help")
