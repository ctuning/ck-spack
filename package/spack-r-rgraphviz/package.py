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


class RRgraphviz(RPackage):
    """Interfaces R with the AT and T graphviz library for plotting
    R graph objects from the graph package."""

    homepage = "http://bioconductor.org/packages/Rgraphviz/"
    url      = "https://git.bioconductor.org/packages/Rgraphviz"

    version('2.20.0', git='https://git.bioconductor.org/packages/Rgraphviz', commit='eface6298150667bb22eac672f1a45e52fbf8c90')

    depends_on('r@3.4.0:3.4.9', when='@2.20.0')
    depends_on('r-graph', type=('build', 'run'))
