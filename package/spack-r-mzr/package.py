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


class RMzr(RPackage):
    """mzR provides a unified API to the common file formats and parsers
       available for mass spectrometry data. It comes with a wrapper for the
       ISB random access parser for mass spectrometry mzXML, mzData and mzML
       files. The package contains the original code written by the ISB, and a
       subset of the proteowizard library for mzML and mzIdentML. The netCDF
       reading code has previously been used in XCMS."""

    homepage = "https://www.bioconductor.org/packages/mzR/"
    url      = "https://git.bioconductor.org/packages/mzR"

    version('2.10.0', git='https://git.bioconductor.org/packages/mzR', commit='a6168b68e48c281e88de9647254a8db1e21df388')

    depends_on('r-biobase', type=('build', 'run'))
    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-protgenerics', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-zlibbioc', type=('build', 'run'))
    depends_on('netcdf')
    depends_on('r@3.4.0:3.4.9', when='@2.10.0')
