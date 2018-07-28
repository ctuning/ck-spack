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


class Zeromq(AutotoolsPackage):
    """ The ZMQ networking/concurrency library and core API """
    homepage = "http://zguide.zeromq.org/"
    url      = "http://download.zeromq.org/zeromq-4.1.2.tar.gz"

    version('develop', branch='master',
            git='https://github.com/zeromq/libzmq.git')
    version('4.2.5', 'a1c95b34384257e986842f4d006957b8',
            url='https://github.com/zeromq/libzmq/releases/download/v4.2.5/zeromq-4.2.5.tar.gz')
    version('4.2.2', '52499909b29604c1e47a86f1cb6a9115')
    version('4.1.4', 'a611ecc93fffeb6d058c0e6edf4ad4fb')
    version('4.1.2', '159c0c56a895472f02668e692d122685')
    version('4.1.1', '0a4b44aa085644f25c177f79dc13f253')
    version('4.0.7', '9b46f7e7b0704b83638ef0d461fd59ab')
    version('4.0.6', 'd47dd09ed7ae6e7fd6f9a816d7f5fdf6')
    version('4.0.5', '73c39f5eb01b9d7eaf74a5d899f1d03d')

    depends_on("libsodium")
    depends_on("libsodium@:1.0.3", when='@:4.1.2')

    depends_on('autoconf', type='build', when='@develop')
    depends_on('automake', type='build', when='@develop')
    depends_on('libtool', type='build', when='@develop')
    depends_on('pkgconfig', type='build')

    conflicts('%gcc@8:', when='@:4.2.2')

    @when('@develop')
    def autoreconf(self, spec, prefix):
        bash = which('bash')
        bash('./autogen.sh')

    def configure_args(self):
        config_args = ['--with-libsodium']
        if 'clang' in self.compiler.cc:
            config_args.append("CFLAGS=-Wno-gnu")
            config_args.append("CXXFLAGS=-Wno-gnu")
        return config_args
