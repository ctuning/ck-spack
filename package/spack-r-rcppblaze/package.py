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


class RRcppblaze(RPackage):
    """'Blaze' is an open-source, high-performance C++ math library for dense
       and sparse arithmetic.

       With its state-of-the-art Smart Expression Template implementation
       'Blaze' combines the elegance and ease of use of a domain-specific
       language with 'HPC'-grade performance, making it one of the most
       intuitive and fastest C++ math libraries available. The 'Blaze'
       library offers: - high performance through the integration of
       'BLAS' libraries and manually tuned 'HPC' math kernels - vectorization
       by 'SSE', 'SSE2', 'SSE3', 'SSSE3', 'SSE4', 'AVX', 'AVX2', 'AVX-512',
       'FMA', and 'SVML' - parallel execution by 'OpenMP', C++11 threads and
       'Boost' threads ('Boost' threads are disabled in 'RcppBlaze') - the
       intuitive and easy to use API of a domain specific language - unified
       arithmetic with dense and sparse vectors and matrices - thoroughly
       tested matrix and vector arithmetic - completely portable, high quality
       C++ source code. The 'RcppBlaze' package includes the header files from
       the 'Blaze' library with disabling some functionalities related to link
       to the thread and system libraries which make 'RcppBlaze' be a
       header-only library. Therefore, users do not need to install 'Blaze'
       and the dependency 'Boost'. 'Blaze' is licensed under the New (Revised)
       BSD license, while 'RcppBlaze' (the 'Rcpp' bindings/bridge to 'Blaze')
       is licensed under the GNU GPL version 2 or later, as is the rest of
       'Rcpp'. Note that since 'Blaze' has committed to 'C++14' commit to
       'C++14' which does not used by most R users from version 3.0, we will
       use the version 2.6 of 'Blaze' which is 'C++98' compatible to support
       the most compilers and system."""

    homepage = "https://github.com/Chingchuan-chen/RcppBlaze"
    url      = "https://cran.rstudio.com/src/contrib/RcppBlaze_0.2.2.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/RcppBlaze"

    version('0.2.2', '22ecae73cf1bebce06ed6387d49f2c77')

    depends_on('r-rcpp@0.11.0:', type=('build', 'run'))
    depends_on('r-matrix@1.1-0:', type=('build', 'run'))
    depends_on('r-bh@1.54.0-2:', type=('build', 'run'))
    depends_on('r@3.0.2:')
