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


class RBrew(RPackage):
    """brew implements a templating framework for mixing text and R code for
    report generation. brew template syntax is similar to PHP, Ruby's erb
    module, Java Server Pages, and Python's psp module."""

    homepage = "https://cran.r-project.org/package=brew"
    url      = "https://cran.r-project.org/src/contrib/brew_1.0-6.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/brew"

    version('1.0-6', '4aaca5e6ec145e0fc0fe6375ce1f3806')
