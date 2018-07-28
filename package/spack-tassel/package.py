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


class Tassel(Package):
    """TASSEL is a software package to evaluate traits associations,
       evolutionary patterns, and linkage disequilibrium."""

    homepage = "http://www.maizegenetics.net/tassel"
    url      = "https://bitbucket.org/tasseladmin/tassel-5-source/get/master.tar.gz"

    version('2017-07-22', git='https://bitbucket.org/tasseladmin/tassel-5-standalone.git',
            commit='ae96ae75c3c9a9e8026140b6c775fa4685bdf531')

    depends_on('java', type=('build', 'run'))
    depends_on('perl', type=('build', 'run'))

    def install(self, spec, prefix):
        install_tree('.', prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('CLASSPATH', prefix.bin.lib)
