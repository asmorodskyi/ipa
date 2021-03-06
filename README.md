[![Build Status](https://travis-ci.com/SUSE-Enceladus/ipa.svg?branch=master)](https://travis-ci.com/SUSE-Enceladus/ipa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/845fb1620f334ae09488e8137dd6d256)](https://www.codacy.com/app/default-org/ipa?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SUSE-Enceladus/ipa&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/ipa/badge/?version=latest)](https://ipa.readthedocs.io/en/latest/?badge=latest)
[![Py Versions](https://img.shields.io/pypi/pyversions/python3-ipa.svg)](https://pypi.org/project/python3-ipa/)
[![License](https://img.shields.io/pypi/l/python3-ipa.svg)](https://pypi.org/project/python3-ipa/)

[![IPA](https://raw.githubusercontent.com/SUSE-Enceladus/ipa/master/docs/source/_images/logo.png "IPA Logo")](https://github.com/SUSE-Enceladus/ipa)

overview
========

**IPA** (Image Proofing App) provides a command line utility to test
images in the Public Cloud (AWS, Azure, GCE, etc.).

With **IPA** you can now test custom images in a provider agnostic way
with one tool and one API. In the first release, **IPA** supports the
openSUSE and SLES distributions. It also supports the three largest
cloud providers (AWS, Azure and GCE). However, it is intended to be
distribution agnostic and framework transparent so both are easily
extensible.

For each distribution there are specific synchronization points that
must be provided. These currently include soft reboot and system update.
The synch points not only test functionality but also act as dividers to
separate distinct sections of a test suite. For example you can run a
test to ensure the proper repos exist before and after a system update.
The system update synch point will guarantee the order of tests.
Speaking of tests, if you're already familiar with Pytest conventions
there's no need to learn a whole new unit testing framework. **IPA** is
written in Python and leverages the Pytest framework through Testinfra.

Installation
============

To install the package use the following commands as root:

```shell
$ zypper ar http://download.opensuse.org/repositories/Cloud:/Tools/<distribution>
$ zypper refresh
$ zypper in python3-ipa
```

Requirements
============

-   apache-libcloud
-   azure-common
-   azure-mgmt-compute
-   azure-mgmt-network
-   azure-mgmt-resource
-   certifi
-   Click
-   cryptography
-   paramiko
-   pycryptodome
-   pytest
-   PyYaml
-   testinfra

# [Docs](https://ipa.readthedocs.io/en/latest/)

Tests
=====

**ipa** uses the Testinfra package for writing unit tests. Testinfra
leverages Pytest and provides modules such as Package, Process and
Service to test the state of images. See the [Testinfra
Docs](https://testinfra.readthedocs.io/en/latest/) for more information
on writing infrastructure tests.

> **ipa** currently passes the Pytest option `-x` (stop on first
> failure) through as `--early-exit`. If there's an interest or need for
> any other options/args please submit an issue to
> [Github](https://github.com/SUSE-Enceladus/ipa/issues).

CLI Overview
============

The CLI provides multiple subcommands to initiate image testing:

* `ipa test`

   Test image in the given framework using the supplied test files.

* `ipa results`

   Invokes the default show subcommand `ipa results show 1`.

* `ipa results clear`

   Clear the results from the history file.

* `ipa results delete`

   Delete the specified history item from the history log.

* ipa results list`

   Display list of results history.

* `ipa results show`

   Display the results or log file for a history item.

* `ipa list`

   Print a list of test files or test cases.

Issues/Enhancements
===================

Please submit issues and requests to
[Github](https://github.com/SUSE-Enceladus/ipa/issues).

Contributing
============

Contributions to **ipa** are welcome and encouraged. See
[CONTRIBUTING](https://github.com/SUSE-Enceladus/ipa/blob/master/CONTRIBUTING.md)
for info on getting started.

License
=======

Copyright (c) 2018 SUSE LLC.

Distributed under the terms of GPL-3.0+ license, see
[LICENSE](https://github.com/SUSE-Enceladus/ipa/blob/master/LICENSE)
for details.
