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


class RAssertthat(RPackage):
    """assertthat is an extension to stopifnot() that makes it easy to declare
    the pre and post conditions that you code should satisfy, while also
    producing friendly error messages so that your users know what they've done
    wrong."""

    homepage = "https://cran.r-project.org/package=assertthat"
    url      = "https://cran.r-project.org/src/contrib/assertthat_0.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/assertthat"
    version('0.2.0', '8134f0072c6a84fd738d3bfc5e7f68ef')
    version('0.1', '59f9d7f7c00077ea54d763b78eeb5798')
