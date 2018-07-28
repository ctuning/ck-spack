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


class RNlme(RPackage):
    """Fit and compare Gaussian linear and nonlinear mixed-effects models."""

    homepage = "https://cran.r-project.org/package=nlme"
    url      = "https://cran.r-project.org/src/contrib/nlme_3.1-130.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/nlme"

    version('3.1-131', '0f1215ec4d4e3bca939282d122f4d1fa')
    version('3.1-130', '1935d6e308a8018ed8e45d25c8731288')
    version('3.1-128', '3d75ae7380bf123761b95a073eb55008')

    depends_on('r-lattice', type=('build', 'run'))
