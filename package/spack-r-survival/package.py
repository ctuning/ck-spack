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


class RSurvival(RPackage):
    """Contains the core survival analysis routines, including definition of
    Surv objects, Kaplan-Meier and Aalen-Johansen (multi-state) curves, Cox
    models, and parametric accelerated failure time models."""

    homepage = "https://cran.r-project.org/package=survival"
    url      = "https://cran.r-project.org/src/contrib/survival_2.41-3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/survival"

    version('2.41-3', '6edb8093d1177775685dc26f3ce78d73')
    version('2.40-1', 'a2474b656cd723791268e3114481b8a7')
    version('2.39-5', 'a3cc6b5762e8c5c0bb9e64a276710be2')

    depends_on('r-matrix', type=('build', 'run'))
