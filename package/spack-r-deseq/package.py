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


class RDeseq(RPackage):
    """Estimate variance-mean dependence in count data from
    high-throughput sequencing assays and test for differential
    expression based on a model using the negative binomial
    distribution."""

    homepage = "https://www.bioconductor.org/packages/DESeq/"
    url      = "https://git.bioconductor.org/packages/DESeq"

    version('1.28.0', git='https://git.bioconductor.org/packages/DESeq', commit='738371466e6ccf00179fd35b617c8ba0e1e91630')

    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-biobase', type=('build', 'run'))
    depends_on('r-locfit', type=('build', 'run'))
    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-genefilter', type=('build', 'run'))
    depends_on('r-geneplotter', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'))
    depends_on('r-rcolorbrewer', type=('build', 'run'))
