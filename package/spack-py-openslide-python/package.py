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


class PyOpenslidePython(PythonPackage):
    """OpenSlide Python is a Python interface to the OpenSlide library."""

    homepage = "https://github.com/openslide/openslide-python"
    url      = "https://github.com/openslide/openslide-python/archive/v1.1.1.tar.gz"

    version('1.1.1', '8c207e48069887b63ea1c7bc9eb7dfc0')

    import_modules = ['openslide']

    depends_on('openslide@3.4.0:')
    depends_on('python@2.6:2.8,3.3:')
    depends_on('py-setuptools', type='build')
    depends_on('py-pillow+jpeg+jpeg2000+tiff', type=('build', 'run'))
