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
import distutils.dir_util


class Snphylo(Package):
    """A pipeline to generate a phylogenetic tree from huge SNP data"""

    homepage = "http://chibba.pgml.uga.edu/snphylo/"
    url      = "http://chibba.pgml.uga.edu/snphylo/snphylo.tar.gz"

    version('2016-02-04', '467660814965bc9bed6c020c05c0d3a6')

    depends_on('python', type=('build', 'run'))
    depends_on('r', type=('build', 'run'))
    depends_on('r-phangorn', type=('build', 'run'))
    depends_on('r-gdsfmt', type=('build', 'run'))
    depends_on('r-snprelate', type=('build', 'run'))
    depends_on('r-getopt', type=('build', 'run'))
    depends_on('muscle')
    depends_on('phylip')

    def install(self, spec, prefix):
        install_answer = ['y', 'y', 'y', 'y']
        install_answer_input = 'spack-config.in'
        with open(install_answer_input, 'w') as f:
            f.writelines(install_answer)
        with open(install_answer_input, 'r') as f:
            bash = which('bash')
            bash('./setup.sh', input=f)
            distutils.dir_util.copy_tree(".", prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.spec.prefix)
