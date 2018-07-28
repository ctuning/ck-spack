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


class PyDlcpar(PythonPackage):
    """DLCpar is a reconciliation method for inferring gene duplications,
    losses, and coalescence (accounting for incomplete lineage sorting)."""

    homepage = "https://www.cs.hmc.edu/~yjw/software/dlcpar/"
    url      = "https://www.cs.hmc.edu/~yjw/software/dlcpar/pub/sw/dlcpar-1.0.tar.gz"

    version('1.0', '0bf684436df3554e46d5e992349eeaec')

    depends_on('py-numpy', type=('build', 'run'))
