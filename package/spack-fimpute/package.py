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


class Fimpute(Package):
    """FImpute uses an overlapping sliding window approach to efficiently
       exploit relationships or haplotype similarities between target and
       reference individuals."""

    homepage = "http://www.aps.uoguelph.ca/~msargol/fimpute/"
    url      = "http://www.aps.uoguelph.ca/~msargol/fimpute/FImpute_Linux.zip"

    version('2014-01', 'df934a25c76dabef7d7afcb5b8058d98')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('FImpute', prefix.bin)
