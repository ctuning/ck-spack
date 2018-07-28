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


class RCoin(RPackage):
    """Conditional inference procedures for the general independence problem
    including two-sample, K-sample (non-parametric ANOVA), correlation,
    censored, ordered and multivariate problems."""

    homepage = "https://cran.r-project.org/package=coin"
    url      = "https://cran.r-project.org/src/contrib/coin_1.1-3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/coin"

    version('1.1-3', '97d3d21f1e4a5762e36dd718dd2d0661')

    depends_on('r@2.14.0:')

    depends_on('r-survival', type=('build', 'run'))
    depends_on('r-modeltools@0.2-9:', type=('build', 'run'))
    depends_on('r-mvtnorm@1.0-5:', type=('build', 'run'))
    depends_on('r-multcomp', type=('build', 'run'))
