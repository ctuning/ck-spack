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


class Mlhka(Package):
    """A maximum likelihood ratio test of natural selection, using polymorphism
       and divergence data."""

    homepage = "https://wright.eeb.utoronto.ca"
    url      = "https://github.com/rossibarra/MLHKA"

    version('2.1', git='https://github.com/rossibarra/MLHKA.git',
            commit='e735ddd39073af58da21b00b27dea203736e5467')

    def install(self, spec, prefix):
        cxx = which('c++')
        cxx('MLHKA_version{0}.cpp'.format(self.version), '-o', 'MLHKA')
        mkdirp(prefix.bin)
        install('MLHKA', prefix.bin)
