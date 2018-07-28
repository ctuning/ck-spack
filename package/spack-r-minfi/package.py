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


class RMinfi(RPackage):
    """Tools to analyze & visualize Illumina Infinium methylation arrays."""

    homepage = "https://bioconductor.org/packages/minfi/"
    url      = "https://git.bioconductor.org/packages/minfi"
    list_url = homepage

    version('1.22.1', git='https://git.bioconductor.org/packages/minfi', commit='b2faf84bcbb291e32d470a0e029450093527545b')

    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-genomicranges', type=('build', 'run'))
    depends_on('r-summarizedexperiment', type=('build', 'run'))
    depends_on('r-biostrings', type=('build', 'run'))
    depends_on('r-bumphunter', type=('build', 'run'))
    depends_on('r-s4vectors', type=('build', 'run'))
    depends_on('r-genomeinfodb', type=('build', 'run'))
    depends_on('r-biobase', type=('build', 'run'))
    depends_on('r-iranges', type=('build', 'run'))
    depends_on('r-beanplot', type=('build', 'run'))
    depends_on('r-rcolorbrewer', type=('build', 'run'))
    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-nor1mix', type=('build', 'run'))
    depends_on('r-siggenes', type=('build', 'run'))
    depends_on('r-limma', type=('build', 'run'))
    depends_on('r-preprocesscore', type=('build', 'run'))
    depends_on('r-illuminaio', type=('build', 'run'))
    depends_on('r-matrixstats', type=('build', 'run'))
    depends_on('r-mclust', type=('build', 'run'))
    depends_on('r-genefilter', type=('build', 'run'))
    depends_on('r-nlme', type=('build', 'run'))
    depends_on('r-reshape', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'))
    depends_on('r-quadprog', type=('build', 'run'))
    depends_on('r-data-table', type=('build', 'run'))
    depends_on('r-geoquery', type=('build', 'run'))
    depends_on('r@3.4.0:3.4.9', when='@1.22.1')
