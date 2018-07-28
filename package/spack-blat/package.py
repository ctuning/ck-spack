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


class Blat(Package):
    """BLAT (BLAST-like alignment tool) is a pairwise sequence
       alignment algorithm."""

    homepage = "https://genome.ucsc.edu/FAQ/FAQblat.html"
    url      = "https://users.soe.ucsc.edu/~kent/src/blatSrc35.zip"

    version('35', '16e546b8843b85e0b0f2fa603cd78724')

    depends_on('libpng')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('MACHTYPE', 'x86_64')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make("BINDIR=%s" % prefix.bin)
