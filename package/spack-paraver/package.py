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
import os


class Paraver(Package):
    """"A very powerful performance visualization and analysis tool
        based on traces that can be used to analyse any information that
        is expressed on its input trace format.  Traces for parallel MPI,
        OpenMP and other programs can be genereated with Extrae."""
    homepage = "https://tools.bsc.es/paraver"
    url = "https://ftp.tools.bsc.es/paraver/wxparaver-4.6.3-src.tar.bz2"

    # NOTE: Paraver provides only latest version for download.
    #       Don't keep/add older versions.
    version('4.6.3', '7940a2651f56712c4e8a21138b4bf16c')
    version('4.6.2', '3f5b3e207d98b2c44101f1ff5685aa55')

    depends_on("boost")
    # depends_on("extrae")
    depends_on("wx")
    depends_on("wxpropgrid")

    def install(self, spec, prefix):
        os.chdir("ptools_common_files")
        configure("--prefix=%s" % prefix)
        make()
        make("install")

        os.chdir("../paraver-kernel")
        # "--with-extrae=%s" % spec['extrae'].prefix,
        configure("--prefix=%s" % prefix,
                  "--with-ptools-common-files=%s" % prefix,
                  "--with-boost=%s" % spec['boost'].prefix,
                  "--with-boost-serialization=boost_serialization")
        make()
        make("install")

        os.chdir("../paraver-toolset")
        configure("--prefix=%s" % prefix)
        make()
        make("install")

        os.chdir("../wxparaver")
        # "--with-extrae=%s" % spec['extrae'].prefix,
        configure("--prefix=%s" % prefix,
                  "--with-paraver=%s" % prefix,
                  "--with-boost=%s" % spec['boost'].prefix,
                  "--with-boost-serialization=boost_serialization",
                  "--with-wxdir=%s" % spec['wx'].prefix.bin)
        make()
        make("install")
