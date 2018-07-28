Collective Knowledge repository for Spack packages
==================================================

[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-powered-by-ck.png)](http://cKnowledge.org)

This repository provides functionality to connect spack packages and CK workflows.
It's an on-going project so please be patient.

Resources:
* [CK framework](http://cKnowledge.org)
* [CK first steps](https://github.com/ctuning/ck/wiki/First-Steps)
* [CK portable workflows](https://github.com/ctuning/ck/wiki/Portable-workflows)
* [Spack](http://spack.io)

License
=======
* CK: BSD, 3-clause
* Spack: LGPL v2.1

Minimal CK installation
=======================

The minimal installation requires:

* Python 2.7 or 3.3+ (limitation is mainly due to unitests)
* Git command line client.

You can install CK in your local user space as follows:

```
$ git clone http://github.com/ctuning/ck
$ export PATH=$PWD/ck/bin:$PATH
$ export PYTHONPATH=$PWD/ck:$PYTHONPATH
```

You can also install CK via PIP with sudo to avoid setting up environment variables yourself:

```
$ sudo pip install ck
```

Usage
=====

Install this repository and dependencies:
```
$ ck pull repo:ck-spack
```

List available packages imported from spack:
```
$ ck ls package:spack-*
```

Install any package such as abinit:
```
$ ck install package:spack-abinit
 or
$ ck install package:spack-abinit --env.PACKAGE_VERSION="8.8.2" --env.SPACK_EXTRA_CMD=""
```

See CK virtual environment for all installed CK packages:
```
$ ck show env
```

Run virtual CK environment:
```
$ ck virtual env --tags=spack,native
```

Feedback and suggestions
========================
* Contact [CK community](https://github.com/ctuning/ck/wiki/Contacts)
* Contact [Spack community](https://groups.google.com/forum/#!forum/spack)
