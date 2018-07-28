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
import fnmatch
import os


class Cosmomc(Package):
    """CosmoMC is a Fortran 2008 Markov-Chain Monte-Carlo (MCMC) engine
       for exploring cosmological parameter space, together with
       Fortran and python code for analysing Monte-Carlo samples and
       importance sampling (plus a suite of scripts for building grids
       of runs, plotting and presenting results)."""

    homepage = "http://cosmologist.info/cosmomc/"
    url      = "https://github.com/cmbant/CosmoMC/archive/Nov2016.tar.gz"

    version('2016.11', '98620cb746352f68fb0c1196e9a070ac')
    version('2016.06', '92dc651d1407cca6ea9228992165f5cb')

    def url_for_version(self, version):
        names = {'2016.11': "Nov2016",
                 '2016.06': "June2016"}
        return ("https://github.com/cmbant/CosmoMC/archive/%s.tar.gz" %
                names[str(version)])

    variant('mpi', default=True, description='Enable MPI support')
    variant('planck', default=False,
            description='Enable Planck Likelihood code and baseline data')
    variant('python', default=True, description='Enable Python bindings')

    extends('python', when='+python')

    depends_on('mpi', when='+mpi')
    depends_on('planck-likelihood', when='+planck')
    depends_on('py-matplotlib', type=('build', 'run'), when='+python')
    depends_on('py-numpy', type=('build', 'run'), when='+python')
    depends_on('py-pandas', type=('build', 'run'), when='+python')
    depends_on('py-scipy', type=('build', 'run'), when='+python')
    depends_on('py-six', type=('build', 'run'), when='+python')
    depends_on('python @2.7:2.999,3.4:', type=('build', 'run'), when='+python')

    patch('Makefile.patch')
    patch('errorstop.patch')

    parallel = False

    def install(self, spec, prefix):
        # Clean up environment to avoid configure problems
        os.environ.pop('LINKMPI', '')
        os.environ.pop('NERSC_HOST', '')
        os.environ.pop('NONCLIKLIKE', '')
        os.environ.pop('PICO', '')
        os.environ.pop('PRECISION', '')
        os.environ.pop('RECOMBINATION', '')
        os.environ.pop('WMAP', '')

        # Set up Planck data if requested
        clikdir = join_path('data', 'clik')
        try:
            os.remove(clikdir)
        except OSError:
            pass
        if '+planck' in spec:
            os.symlink(join_path(os.environ['CLIK_DATA'], 'plc_2.0'), clikdir)
        else:
            os.environ.pop('CLIK_DATA', '')
            os.environ.pop('CLIK_PATH', '')
            os.environ.pop('CLIK_PLUGIN', '')

        # Choose compiler
        # Note: Instead of checking the compiler vendor, we should
        # rewrite the Makefile to use Spack's options all the time
        if spec.satisfies('%gcc'):
            if not spec.satisfies('%gcc@6:'):
                raise InstallError(
                    "When using GCC, "
                    "CosmoMC requires version gcc@6: for building")
            choosecomp = 'ifortErr=1'       # choose gfortran
        elif spec.satisfies('%intel'):
            if not spec.satifies('%intel@14:'):
                raise InstallError(
                    "When using the Intel compiler, "
                    "CosmoMC requires version intel@14: for building")
            choosecomp = 'ifortErr=0'       # choose ifort
        else:
            raise InstallError("Only GCC and Intel compilers are supported")

        # Configure MPI
        if '+mpi' in spec:
            wantmpi = 'BUILD=MPI'
            mpif90 = 'MPIF90C=%s' % spec['mpi'].mpifc
        else:
            wantmpi = 'BUILD=NOMPI'
            mpif90 = 'MPIF90C='

        # Choose BLAS and LAPACK
        lapack = ("LAPACKL=%s" %
                  (spec['lapack'].libs + spec['blas'].libs).ld_flags)

        # Build
        make(choosecomp, wantmpi, mpif90, lapack)

        # Install
        mkdirp(prefix.bin)
        install('cosmomc', prefix.bin)
        root = join_path(prefix.share, 'cosmomc')
        mkdirp(root)
        entries = [
            'batch1',
            'batch2',
            'batch3',
            'camb',
            'chains',
            'clik_latex.paramnames',
            'clik_units.paramnames',
            'cosmomc.cbp',
            'data',
            'distgeneric.ini',
            'distparams.ini',
            'disttest.ini',
            'docs',
            'job_script',
            'job_script_MOAB',
            'job_script_SLURM',
            'paramnames',
            'params_generic.ini',
            'planck_covmats',
            'scripts',
            # don't copy 'source'
            'test.ini',
            'test_pico.ini',
            'test_planck.ini',
            'tests',
        ]
        if '+python' in spec:
            entries += ['python']
        for entry in entries:
            if os.path.isfile(entry):
                install(entry, root)
            else:
                install_tree(entry, join_path(root, entry))
        for dirpath, dirnames, filenames in os.walk(prefix):
            for filename in fnmatch.filter(filenames, '*~'):
                os.remove(os.path.join(dirpath, filename))

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def check_install(self):
        prefix = self.prefix
        spec = self.spec

        os.environ.pop('LINKMPI', '')
        os.environ.pop('NERSC_HOST', '')
        os.environ.pop('NONCLIKLIKE', '')
        os.environ.pop('PICO', '')
        os.environ.pop('PRECISION', '')
        os.environ.pop('RECOMBINATION', '')
        os.environ.pop('WMAP', '')

        os.environ.pop('COSMOMC_LOCATION', '')
        os.environ.pop('PLC_LOCATION', '')

        os.environ.pop('CLIKPATH', '')
        os.environ.pop('PLANCKLIKE', '')

        exe = spec['cosmomc'].command.path
        args = []
        if '+mpi' in spec:
            # Add mpirun prefix
            args = ['-np', '1', exe]
            exe = join_path(spec['mpi'].prefix.bin, 'mpiexec')
        cosmomc = Executable(exe)
        with working_dir('spack-check', create=True):
            for entry in [
                'camb',
                'chains',
                'data',
                'paramnames',
                'planck_covmats',
            ]:
                os.symlink(join_path(prefix.share, 'cosmomc', entry), entry)
            inifile = join_path(prefix.share, 'cosmomc', 'test.ini')
            cosmomc(*(args + [inifile]))
            if '+planck' in spec:
                inifile = join_path(prefix.share, 'cosmomc', 'test_planck.ini')
                cosmomc(*(args + [inifile]))
