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


class RAffypdnn(RPackage):
    """The package contains functions to perform the PDNN method
    described by Li Zhang et al."""

    homepage = "https://www.bioconductor.org/packages/affypdnn/"
    url      = "https://git.bioconductor.org/packages/affypdnn"

    version('1.50.0', git='https://git.bioconductor.org/packages/affypdnn', commit='97ff68e9f51f31333c0330435ea23b212b3ed18a')

    depends_on('r@3.4.0:3.4.9', when='@1.50.0')
    depends_on('r-affy', type=('build', 'run'))
