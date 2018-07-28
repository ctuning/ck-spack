#
# Collective Knowledge (spack API)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# import spack packages

def import_func(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import shutil
    import copy

    o=i.get('out','')

    oo=''
    if o=='con': oo=o

    # Load package meta template
    pt=os.path.join(work['path'],'package_meta_template.json')
    r=ck.load_json_file({'json_file':pt})
    if r['return']>0: return r
    dd=r['dict']
    ddd=copy.deepcopy(dd)

    # Set env for spack to download it and get path
    r=ck.access({'action':'set',
                 'module_uoa':cfg['module_deps']['env'],
                 'tags':'tool,spack',
                 'out':oo})
    if r['return']>0: return r

    d=r['dict']

    env=d.get('env',{})

    p=env.get('CK_ENV_TOOL_SPACK','')

    if p=='' or not os.path.isdir(p):
       return {'return':1, 'error':'path to spack not found'}

    # Get path to packages
    pp=os.path.join(p, 'var', 'spack', 'repos', 'builtin', 'packages')

    d=os.listdir(pp)
    for package in sorted(d):
        ck.out('Processing '+package+' ...')

        dd=copy.deepcopy(ddd)

        dd['tags'].append(package)

        dd['suggested_path']+=package

        dd['customize']['install_env']['SPACK_PACKAGE_NAME']=package

        dd['package_extra_name']=' ('+package+', native)'

        r=ck.access({'action':'update',
                     'module_uoa':cfg['module_deps']['package'],
                     'data_uoa':'spack-'+package,
                     'repo_uoa':'ck-spack',
                     'dict':dd,
                     'sort_keys':'yes',
                     'substitute':'yes',
                     'ignore_update':'yes'})
        if r['return']>0: return r

        pn=r['path']

        pp1=os.path.join(pp, package, 'package.py')
        pn1=os.path.join(pn, 'package.py')

        shutil.copyfile(pp1,pn1)


    return {'return':0}
