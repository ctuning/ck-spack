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


class RScales(RPackage):
    """Graphical scales map data to aesthetics, and provide methods for
    automatically determining breaks and labels for axes and legends."""

    homepage = "https://github.com/hadley/scales"
    url      = "https://cran.r-project.org/src/contrib/scales_0.5.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/scales"

    version('0.5.0', '435f6bd826c5cf8df703ffb8a6750fd1')
    version('0.4.1', '3fb2218866a7fe4c1f6e66790876f85a')
    version('0.4.0', '7b5602d9c55595901192248bca25c099')

    depends_on('r-rcolorbrewer', type=('build', 'run'))
    depends_on('r-dichromat', type=('build', 'run'))
    depends_on('r-plyr', type=('build', 'run'))
    depends_on('r-munsell', type=('build', 'run'))
    depends_on('r-labeling', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-r6', type=('build', 'run'))
    depends_on('r-viridislite', type=('build', 'run'))
