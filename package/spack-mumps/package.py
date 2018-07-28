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
import os
import sys
import glob


class Mumps(Package):
    """MUMPS: a MUltifrontal Massively Parallel sparse direct Solver"""

    homepage = "http://mumps.enseeiht.fr"
    url      = "http://mumps.enseeiht.fr/MUMPS_5.0.1.tar.gz"

    version('5.1.1', 'f15c6b5dd8c71b1241004cd19818259d')
    version('5.0.2', '591bcb2c205dcb0283872608cdf04927')
    # Alternate location if main server is down.
    # version('5.0.1', 'b477573fdcc87babe861f62316833db0', url='http://pkgs.fedoraproject.org/repo/pkgs/MUMPS/MUMPS_5.0.1.tar.gz/md5/b477573fdcc87babe861f62316833db0/MUMPS_5.0.1.tar.gz')
    version('5.0.1', 'b477573fdcc87babe861f62316833db0')

    variant('mpi', default=True,
            description='Compile MUMPS with MPI support')
    variant('scotch', default=False,
            description='Activate Scotch as a possible ordering library')
    variant('ptscotch', default=False,
            description='Activate PT-Scotch as a possible ordering library')
    variant('metis', default=False,
            description='Activate Metis as a possible ordering library')
    variant('parmetis', default=False,
            description='Activate Parmetis as a possible ordering library')
    variant('double', default=True,
            description='Activate the compilation of dmumps')
    variant('float', default=True,
            description='Activate the compilation of smumps')
    variant('complex', default=True,
            description='Activate the compilation of cmumps and/or zmumps')
    variant('int64', default=False,
            description='Use int64_t/integer*8 as default index type')
    variant('shared', default=True, description='Build shared libraries')

    depends_on('scotch + esmumps', when='~ptscotch+scotch')
    depends_on('scotch + esmumps ~ metis + mpi', when='+ptscotch')
    depends_on('metis@5:', when='+metis')
    depends_on('parmetis', when="+parmetis")
    depends_on('blas')
    depends_on('lapack')
    depends_on('scalapack', when='+mpi')
    depends_on('mpi', when='+mpi')

    patch('mumps-5.0.2-spectrum-mpi-xl.patch', when='@5.0.2%xl^spectrum-mpi')
    patch('mumps-5.0.2-spectrum-mpi-xl.patch', when='@5.0.2%xl_r^spectrum-mpi')
    patch('mumps-5.1.1-spectrum-mpi-xl.patch', when='@5.1.1%xl^spectrum-mpi')
    patch('mumps-5.1.1-spectrum-mpi-xl.patch', when='@5.1.1%xl_r^spectrum-mpi')

    # this function is not a patch function because in case scalapack
    # is needed it uses self.spec['scalapack'].fc_link set by the
    # setup_dependent_environment in scalapck. This happen after patch
    # end before install
    # def patch(self):
    def write_makefile_inc(self):
        if ('+parmetis' in self.spec or '+ptscotch' in self.spec) and (
                '+mpi' not in self.spec):
            raise RuntimeError(
                'You cannot use the variants parmetis or ptscotch without mpi')

        # The makefile variables LIBBLAS, LSCOTCH, LMETIS, and SCALAP are only
        # used to link the examples, so if building '+shared' there is no need
        # to explicitly link with the respective libraries because we make sure
        # the mumps shared libraries are already linked with them. See also the
        # comment below about 'inject_libs'. This behaviour may cause problems
        # if building '+shared' and the used libraries were build static
        # without the PIC option.
        shared = '+shared' in self.spec

        lapack_blas = (self.spec['lapack'].libs + self.spec['blas'].libs)
        makefile_conf = ["LIBBLAS = %s" %
                         lapack_blas.ld_flags if not shared else '']

        orderings = ['-Dpord']

        if '+ptscotch' in self.spec or '+scotch' in self.spec:
            makefile_conf.extend([
                "ISCOTCH = -I%s" % self.spec['scotch'].prefix.include,
                "LSCOTCH = {0}".format(
                    self.spec['scotch'].libs.ld_flags if not shared else '')
            ])

            orderings.append('-Dscotch')
            if '+ptscotch' in self.spec:
                orderings.append('-Dptscotch')

        if '+parmetis' in self.spec and '+metis' in self.spec:
            makefile_conf.extend([
                "IMETIS = -I%s" % self.spec['parmetis'].prefix.include,
                ("LMETIS = -L%s -l%s -L%s -l%s" % (
                    self.spec['parmetis'].prefix.lib, 'parmetis',
                    self.spec['metis'].prefix.lib, 'metis')) if not shared
                else 'LMETIS ='
            ])

            orderings.append('-Dparmetis')
        elif '+metis' in self.spec:
            makefile_conf.extend([
                "IMETIS = -I%s" % self.spec['metis'].prefix.include,
                ("LMETIS = -L%s -l%s" % (
                    self.spec['metis'].prefix.lib, 'metis')) if not shared
                else 'LMETIS ='
            ])

            orderings.append('-Dmetis')

        makefile_conf.append("ORDERINGSF = %s" % (' '.join(orderings)))

        # when building shared libs need -fPIC, otherwise
        # /usr/bin/ld: graph.o: relocation R_X86_64_32 against `.rodata.str1.1'
        # can not be used when making a shared object; recompile with -fPIC
        fpic = self.compiler.pic_flag if '+shared' in self.spec else ''
        # TODO: test this part, it needs a full blas, scalapack and
        # partitionning environment with 64bit integers

        using_xl = self.compiler.name in ['xl', 'xl_r']
        if '+int64' in self.spec:
            if self.compiler.name == "xl" or self.compiler.name == "xl_r":
                makefile_conf.extend(
                    ['OPTF    = -O3',
                     'OPTL    = %s -O3' % fpic,
                     'OPTC    = %s -O3-DINTSIZE64' % fpic])
            else:
                makefile_conf.extend(
                    # the fortran compilation flags most probably are
                    # working only for intel and gnu compilers this is
                    # perhaps something the compiler should provide
                    ['OPTF    = %s -O  -DALLOW_NON_INIT %s' % (fpic, '-fdefault-integer-8' if self.compiler.name == "gcc" else '-i8'),  # noqa
                     'OPTL    = %s -O ' % fpic,
                     'OPTC    = %s -O -DINTSIZE64' % fpic])
        else:
            if using_xl:
                makefile_conf.extend(
                    ['OPTF    = -O3 -qfixed',
                     'OPTL    = %s -O3' % fpic,
                     'OPTC    = %s -O3' % fpic])
            else:
                makefile_conf.extend(
                    ['OPTF    = %s -O  -DALLOW_NON_INIT' % fpic,
                     'OPTL    = %s -O ' % fpic,
                     'OPTC    = %s -O ' % fpic])

        if '+mpi' in self.spec:
            scalapack = self.spec['scalapack'].libs if not shared \
                else LibraryList([])
            makefile_conf.extend(
                ['CC = {0}'.format(self.spec['mpi'].mpicc),
                 'FC = {0}'.format(self.spec['mpi'].mpifc),
                 "SCALAP = %s" % scalapack.ld_flags,
                 "MUMPS_TYPE = par"])
            # The FL makefile variable is used for linking the examples and
            # linking the shared mumps libraries (in some cases).
            if using_xl and self.spec.satisfies('^spectrum-mpi'):
                makefile_conf.extend(
                    ['FL = {0}'.format(self.spec['mpi'].mpicc)])
            else:
                makefile_conf.extend(
                    ['FL = {0}'.format(self.spec['mpi'].mpifc)])
        else:
            makefile_conf.extend(
                ["CC = cc",
                 "FC = fc",
                 "FL = fc",
                 "MUMPS_TYPE = seq"])

        # TODO: change the value to the correct one according to the
        # compiler possible values are -DAdd_, -DAdd__ and/or -DUPPER
        if self.compiler.name == 'intel' or self.compiler.name == 'pgi':
            # Intel & PGI Fortran compiler provides the main() function so
            # C examples linked with the Fortran compiler require a
            # hack defined by _DMAIN_COMP (see examples/c_example.c)
            makefile_conf.append("CDEFS   = -DAdd_ -DMAIN_COMP")
        else:
            if not using_xl:
                makefile_conf.append("CDEFS   = -DAdd_")

        if '+shared' in self.spec:
            # All Mumps libraries will be linked with 'inject_libs'.
            inject_libs = []
            if '+mpi' in self.spec:
                inject_libs += [self.spec['scalapack'].libs.ld_flags]
            if '+ptscotch' in self.spec or '+scotch' in self.spec:
                inject_libs += [self.spec['scotch'].libs.ld_flags]
            if '+parmetis' in self.spec and '+metis' in self.spec:
                inject_libs += [
                    "-L%s -l%s -L%s -l%s" % (
                        self.spec['parmetis'].prefix.lib, 'parmetis',
                        self.spec['metis'].prefix.lib, 'metis')]
            elif '+metis' in self.spec:
                inject_libs += [
                    "-L%s -l%s" % (self.spec['metis'].prefix.lib, 'metis')]
            inject_libs += [lapack_blas.ld_flags]
            inject_libs = ' '.join(inject_libs)

            if sys.platform == 'darwin':
                # Building dylibs with mpif90 causes segfaults on 10.8 and
                # 10.10. Use gfortran. (Homebrew)
                makefile_conf.extend([
                    'LIBEXT=.dylib',
                    'AR=%s -dynamiclib -Wl,-install_name -Wl,%s/$(notdir $@)'
                    ' -undefined dynamic_lookup %s -o ' %
                    (os.environ['FC'], prefix.lib, inject_libs),
                    'RANLIB=echo'
                ])
            else:
                makefile_conf.extend([
                    'LIBEXT=.so',
                    'AR=link_cmd() { $(FL) -shared -Wl,-soname '
                    '-Wl,%s/$(notdir $@) -o "$$@" %s; }; link_cmd ' %
                    (prefix.lib, inject_libs),
                    'RANLIB=ls'
                ])
                # When building libpord, read AR from Makefile.inc instead of
                # going through the make command line - this prevents various
                # problems with the substring "$$@".
                filter_file(' AR="\$\(AR\)"', '', 'Makefile')
                filter_file('^(INCLUDES = -I../include)',
                            '\\1\ninclude ../../Makefile.inc',
                            join_path('PORD', 'lib', 'Makefile'))

                if using_xl:
                    # The patches for xl + spectrum-mpi use SAR for linking
                    # libpord.
                    makefile_conf.extend([
                        'SAR=%s -shared -Wl,-soname -Wl,%s/$(notdir $@) %s -o'
                        % (env['CC'], prefix.lib, inject_libs)
                    ])
        else:
            makefile_conf.extend([
                'LIBEXT  = .a',
                'AR = ar vr',
                'RANLIB = ranlib'
            ])

        makefile_inc_template = join_path(
            os.path.dirname(self.module.__file__), 'Makefile.inc')
        with open(makefile_inc_template, "r") as fh:
            makefile_conf.extend(fh.read().split('\n'))

        with working_dir('.'):
            with open("Makefile.inc", "w") as fh:
                makefile_inc = '\n'.join(makefile_conf)
                fh.write(makefile_inc)

    def install(self, spec, prefix):
        self.write_makefile_inc()

        # Build fails in parallel
        # That is why we split the builds of 's', 'c', 'd', and/or 'z' which
        # can be build one after the other, each using a parallel build.
        letters_variants = [
            ['s', '+float'], ['c', '+complex+float'],
            ['d', '+double'], ['z', '+complex+double']]
        for l, v in letters_variants:
            if v in spec:
                make(l + 'examples')

        install_tree('lib', prefix.lib)
        install_tree('include', prefix.include)

        if '~mpi' in spec:
            lib_dsuffix = '.dylib' if sys.platform == 'darwin' else '.so'
            lib_suffix = lib_dsuffix if '+shared' in spec else '.a'
            install('libseq/libmpiseq%s' % lib_suffix, prefix.lib)
            for f in glob.glob(join_path('libseq', '*.h')):
                install(f, prefix.include)

        # FIXME: extend the tests to mpirun -np 2 when build with MPI
        # FIXME: use something like numdiff to compare output files
        # Note: In some cases, when 'mpi' is enabled, the examples below cannot
        # be run without 'mpirun', so we enabled the tests only if explicitly
        # requested with the Spack '--test' option.
        if self.run_tests:
            with working_dir('examples'):
                if '+float' in spec:
                    ssimpletest = Executable('./ssimpletest')
                    ssimpletest(input='input_simpletest_real')
                    if '+complex' in spec:
                        csimpletest = Executable('./csimpletest')
                        csimpletest(input='input_simpletest_cmplx')
                if '+double' in spec:
                    dsimpletest = Executable('./dsimpletest')
                    dsimpletest(input='input_simpletest_real')
                    if '+complex' in spec:
                        zsimpletest = Executable('./zsimpletest')
                        zsimpletest(input='input_simpletest_cmplx')

    @property
    def libs(self):
        component_libs = ['*mumps*', 'pord']
        return find_libraries(['lib' + comp for comp in component_libs],
                              root=self.prefix.lib,
                              shared=('+shared' in self.spec),
                              recursive=False) or None
