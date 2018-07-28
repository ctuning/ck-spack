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
import os

from spack import *
from spack.environment import EnvironmentModifications


class IntelIpp(IntelPackage):
    """Intel Integrated Performance Primitives."""

    homepage = "https://software.intel.com/en-us/intel-ipp"

    version('2018.2.199', 'f87276b485d2f6ec070c1b41ac1ed871',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/12726/l_ipp_2018.2.199.tgz')
    version('2018.1.163', '183d4888f3d91f632b617fdd401f04ed',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/12414/l_ipp_2018.1.163.tgz')
    version('2018.0.128', 'e64190bc9041b52d9eed7e8ee91bf1de',
            url='http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/12071/l_ipp_2018.0.128.tgz')
    version('2017.3.196', '47e53bd1a2740041f4d0be7c36b61a18',
            url="http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11545/l_ipp_2017.3.196.tgz")
    version('2017.2.174', '8ad7753ee30c5176c4931070334144bc',
            url="http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11307/l_ipp_2017.2.174.tgz")
    version('2017.1.132', '9fbbaa402b8d16f4cb4be9aee2f557c2',
            url="http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/11031/l_ipp_2017.1.132.tgz")
    version('2017.0.098', 'e7be757ebe351d9f9beed7efdc7b7118',
            url="http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9663/l_ipp_2017.0.098.tgz")
    version('9.0.3.210', '0e1520dd3de7f811a6ef6ebc7aa429a3',
            url="http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/9067/l_ipp_9.0.3.210.tgz")

    provides('ipp')

    @property
    def license_required(self):
        # The Intel libraries are provided without requiring a license as of
        # version 2017.2. Trying to specify the license will fail. See:
        # https://software.intel.com/en-us/articles/free-ipsxe-tools-and-libraries
        if self.version >= Version('2017.2'):
            return False
        else:
            return True

    def setup_environment(self, spack_env, run_env):
        """Adds environment variables to the generated module file.

        These environment variables come from running:

        .. code-block:: console

           $ source ipp/bin/ippvars.sh intel64
        """
        # NOTE: Spack runs setup_environment twice, once pre-build to set up
        # the build environment, and once post-installation to determine
        # the environment variables needed at run-time to add to the module
        # file. The script we need to source is only present post-installation,
        # so check for its existence before sourcing.
        # TODO: At some point we should split setup_environment into
        # setup_build_environment and setup_run_environment to get around
        # this problem.
        ippvars = os.path.join(self.prefix.ipp.bin, 'ippvars.sh')

        if os.path.isfile(ippvars):
            run_env.extend(EnvironmentModifications.from_sourcing_file(
                ippvars, 'intel64'))
