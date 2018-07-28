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
from os import listdir


class Cntk1bitsgd(Package):
    """CNTK1bitSGD is the header-only
    1-bit stochastic gradient descent (1bit-SGD) library for
    the Computational Network Toolkit (CNTK)."""

    homepage = "https://github.com/CNTK-components/CNTK1bitSGD"

    version('master', git='https://github.com/CNTK-components/CNTK1bitSGD.git')
    version('c8b77d', git='https://github.com/CNTK-components/CNTK1bitSGD.git',
            commit='c8b77d6e325a4786547b27624890276c1483aed1')

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        for file in listdir('.'):
            if file.endswith('.h'):
                install(file, prefix.include)
