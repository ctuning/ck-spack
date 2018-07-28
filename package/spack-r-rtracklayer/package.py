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


class RRtracklayer(RPackage):
    """Extensible framework for interacting with multiple genome browsers
       (currently UCSC built-in) and manipulating annotation tracks in various
       formats (currently GFF, BED, bedGraph, BED15, WIG, BigWig and 2bit
       built-in). The user may export/import tracks to/from the supported
       browsers, as well as query and modify the browser state, such as the
       current viewport."""

    homepage = "http://bioconductor.org/packages/rtracklayer/"
    url      = "https://git.bioconductor.org/packages/rtracklayer"
    list_url = homepage

    version('1.36.6', git='https://git.bioconductor.org/packages/rtracklayer', commit='8c0ac7230f94e0c5a981acbb178c8de70e968131')

    depends_on('r-xml', type=('build', 'run'))
    depends_on('r-biocgenerics', type=('build', 'run'))
    depends_on('r-s4vectors', type=('build', 'run'))
    depends_on('r-iranges', type=('build', 'run'))
    depends_on('r-xvector', type=('build', 'run'))
    depends_on('r-genomeinfodb', type=('build', 'run'))
    depends_on('r-biostrings', type=('build', 'run'))
    depends_on('r-zlibbioc', type=('build', 'run'))
    depends_on('r-rcurl', type=('build', 'run'))
    depends_on('r-rsamtools', type=('build', 'run'))
    depends_on('r-genomicalignments', type=('build', 'run'))
    depends_on('r@3.4.0:3.4.9', when='@1.36.6')
