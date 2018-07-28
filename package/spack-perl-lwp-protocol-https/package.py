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


class PerlLwpProtocolHttps(PerlPackage):
    """ Provide https support for LWP::UserAgent"""

    homepage = "http://search.cpan.org/~gaas/LWP-Protocol-https-6.04/lib/LWP/Protocol/https.pm"
    url      = "http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/LWP-Protocol-https-6.04.tar.gz"

    version('6.04', '1b422a7d3b5fed1eb4d748fdc9fd79a4')

    depends_on('perl-test-requiresinternet', type=('build', 'run'))
    depends_on('perl-io-socket-ssl', type=('build', 'run'))
    depends_on('perl-net-http', type=('build', 'run'))
    depends_on('perl-mozilla-ca', type=('build', 'run'))
    depends_on('perl-lwp', type=('build', 'run'))
