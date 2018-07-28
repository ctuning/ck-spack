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
#
# This is a based largely on the Homebrew science formula:
# https://github.com/Homebrew/homebrew-science/blob/master/blast.rb
#
# There s one tricky bit to be resolved:
#
# - HDF5 builds explode, blast's configure script tries to run a program that
#   uses a variable called 'HOST' but some other bit defines a macro called
#   HOST that's defined to a string.  Hilarity ensues.
#
#
from spack import *


class BlastPlus(AutotoolsPackage):
    """Basic Local Alignment Search Tool."""

    homepage = "http://blast.ncbi.nlm.nih.gov/"
    url      = "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-blast-2.6.0+-src.tar.gz"

    version('2.6.0',  'c8ce8055b10c4d774d995f88c7cc6225')
    version('2.2.30', 'f8e9a5eb368173142fe6867208b73715')

    # homebrew sez: Fixed upstream in future version > 2.6
    # But this bug sez that it will be fixed in 2.6
    #    https://github.com/Homebrew/homebrew-science/pull/4740
    # The 2.6.0 src still matches the "before" bit of the patch
    # so it's probably still "needed".
    # On the other hand, the `find` command is broken and there
    # aren't any .svn dirs in the tree, so I've updated their patch
    # to just comment out the block.
    patch('blast-make-fix2.5.0.diff', when="@2.5.0:2.6.0")

    # See https://github.com/Homebrew/homebrew-science/issues/2337#issuecomment-170011511
    @when('@:2.2.31')
    def patch(self):
        filter_file("2.95* | 2.96* | 3.* | 4.* )",
                    "2.95* | 2.96* | 3.* | 4.* | 5.* )",
                    "c++/src/build-system/configure",
                    string=True)

    # No...
    # depends_on :mysql => :optional

    variant('static', default=False,
            description='Build with static linkage')
    variant('jpeg', default=True,
            description='Build with jpeg support')
    variant('png', default=True,
            description='Build with png support')
    variant('freetype', default=True,
            description='Build with freetype support')
    # variant('hdf5', default=True,
    #        description='Build with hdf5 support')
    variant('gnutls', default=True,
            description='Build with gnutls support')
    variant('openssl', default=True,
            description='Build with openssl support')
    variant('zlib', default=True,
            description='Build with zlib support')
    variant('bzip2', default=True,
            description='Build with bzip2 support')
    variant('lzo', default=True,
            description='Build with lzo support')
    variant('pcre', default=True,
            description='Build with pcre support')
    variant('perl', default=True,
            description='Build with perl support')
    variant('python', default=True,
            description='Build with python support')

    depends_on('jpeg', when='+jpeg')
    depends_on('libpng', when='+png')
    depends_on('freetype', when='+freetype')
    # depends_on('hdf5', when='+hdf5')
    depends_on('gnutls', when='+gnutls')
    depends_on('openssl', when='+openssl')
    depends_on('zlib', when='+zlib')
    depends_on('bzip2', when='+bzip2')
    depends_on('lzo', when='+lzo')
    depends_on('pcre', when='+pcre')

    depends_on('python', when='+python')
    depends_on('perl', when='+perl')

    configure_directory = 'c++'

    def configure_args(self):
        spec   = self.spec

        config_args = [
            '--with-bin-release',
            '--without-debug',
            '--with-mt',
            '--with-64',
            '--without-boost',
        ]

        if '+static' in spec:
            config_args.append('--with-static')
            # FIXME
            # args << "--with-static-exe" unless OS.linux?
            # args << "--with-dll" if build.with? "dll"
        else:
            config_args.extend([
                '--with-dll',
                '--without-static',
                '--without-static-exe'
            ])

        if '+jpeg' in spec:
            config_args.append(
                '--with-jpeg={0}'.format(self.spec['jpeg'].prefix)
            )
        else:
            config_args.append('--without-jpeg')

        if '+png' in spec:
            config_args.append(
                '--with-png={0}'.format(self.spec['libpng'].prefix)
            )
        else:
            config_args.append('--without-png')

        if '+freetype' in spec:
            config_args.append(
                '--with-freetype={0}'.format(self.spec['freetype'].prefix)
            )
        else:
            config_args.append('--without-freetype')

        config_args.append('--without-hdf5')
        # if '+hdf5' in spec:
        #     # FIXME
        #     config_args.append(
        #         '--with-hdf5={0}'.format(self.spec['hdf5'].prefix)
        #     )
        # else:
        #     config_args.append('--without-hdf5')

        if '+zlib' in spec:
            config_args.append(
                '--with-z={0}'.format(self.spec['zlib'].prefix)
            )
        else:
            config_args.append('--without-z')

        if '+bzip2' in spec:
            config_args.append(
                '--with-bz2={0}'.format(self.spec['bzip2'].prefix)
            )
        else:
            config_args.append('--without-bz2')

        if '+lzo' in spec:
            config_args.append(
                '--with-lzo={0}'.format(self.spec['lzo'].prefix)
            )
        else:
            config_args.append('--without-lzo')

        if '+gnutls' in spec:
            config_args.append(
                '--with-gnutls={0}'.format(self.spec['gnutls'].prefix)
            )
        else:
            config_args.append('--without-gnutls')

        if '+openssl' in spec:
            config_args.append(
                '--with-openssl={0}'.format(self.spec['openssl'].prefix)
            )
        else:
            config_args.append('--without-openssl')

        if '+pcre' in spec:
            config_args.append(
                '--with-pcre={0}'.format(self.spec['pcre'].prefix)
            )
        else:
            config_args.append('--without-pcre')

        if '+python' in spec:
            config_args.append(
                '--with-python={0}'.format(self.spec['python'].home)
            )
        else:
            config_args.append('--without-python')

        if '+perl' in spec:
            config_args.append(
                '--with-perl={0}'.format(self.spec['perl'].prefix)
            )
        else:
            config_args.append('--without-python')

        return config_args
