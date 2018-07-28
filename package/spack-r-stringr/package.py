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


class RStringr(RPackage):
    """A consistent, simple and easy to use set of wrappers around the
    fantastic 'stringi' package. All function and argument names (and
    positions) are consistent, all functions deal with "NA"'s and zero length
    vectors in the same way, and the output from one function is easy to feed
    into the input of another."""

    homepage = "https://cran.r-project.org/web/packages/stringr/index.html"
    url      = "https://cran.r-project.org/src/contrib/stringr_1.1.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/stringr"

    version('1.2.0', '9054b1de91c578cc5cf454d656e9c697')
    version('1.1.0', '47973a33944c6d5db9524b1e835b8a5d')
    version('1.0.0', '5ca977c90351f78b1b888b379114a7b4')

    depends_on('r-stringi', type=('build', 'run'))
    depends_on('r-magrittr', type=('build', 'run'))
