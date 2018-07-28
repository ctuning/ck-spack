#
# Collective Knowledge (setup native spack environment via CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net/research
#

import os

##############################################################################
# customize directories to automatically find and register software

def dirs(i):
    return {'return':0}

##############################################################################
# get version from path

def version_cmd(i):

    ck=i['ck_kernel']

    fp=i['full_path']

    # Load ck-spack.json
    r=ck.load_json_file({'json_file':fp})
    if r['return']>0: return r
    d=r['dict']

    ver=d.get('PACKAGE_VERSION','')

    return {'return':0, 'cmd':'', 'version':ver}

##############################################################################
# setup environment

def setup(i):

    s=''

    cus=i['customize']
    env=i['env']

    fp=cus.get('full_path','')

    ep=cus['env_prefix']
    if ep!='' and fp!='':
       # Load ck-spack.json
       r=ck.load_json_file({'json_file':fp})
       if r['return']>0: return r
       d=r['dict']

       spack_root=d.get('SPACK_ROOT','')
       spack_dir=d.get('SPACK_DIR','')
       spack_src=d.get('SPACK_SRC','')
       spack_package_name=d.get('SPACK_PACKAGE_NAME','')

       cspack_package_name=spack_package_name.upper()

       ep+='_'+cspack_package_name

       p1=os.path.dirname(fp)

       env[ep]=p1
       env[ep+'_SPACK_ROOT']=spack_root
       env[ep+'_SPACK_DIR']=spack_dir
       env[ep+'_SPACK_SRC']=spack_src
       env[ep+'_PACKAGE_NAME']=spack_package_name

    return {'return':0, 'bat':s}
