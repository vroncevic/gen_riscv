Generate RISC-V Project
------------------------

**gen_riscv** is tool for generation of RISC-V project.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_riscv python checker| |gen_riscv python package| |github issues| |documentation status| |github contributors|

.. |gen_riscv python checker| image:: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python_checker.yml

.. |gen_riscv python package| image:: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_riscv.svg
   :target: https://github.com/vroncevic/gen_riscv/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_riscv.svg
   :target: https://github.com/vroncevic/gen_riscv/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-riscv/badge/?version=latest
    :target: https://gen-riscv.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_riscv python3 build|

.. |gen_riscv python3 build| image:: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_riscv/actions/workflows/gen_riscv_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_riscv/releases

To install **gen_riscv** type the following

.. code-block:: bash

    tar xvzf gen_riscv-x.y.z.tar.gz
    cd gen_riscv-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_riscv-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_riscv_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_riscv_run.py /usr/local/bin/gen_riscv_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_riscv

Dependencies
-------------

**gen_riscv** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_riscv** is based on OOP

Code structure

.. code-block:: bash

    gen_riscv/
        ├── conf
        │   ├── gen_riscv.cfg
        │   ├── gen_riscv.logo
        │   ├── gen_riscv_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── cflags.template
        │       ├── csflags.template
        │       ├── main.template
        │       ├── Makefile.template
        │       ├── objects.template
        │       ├── odflags.template
        │       ├── sources.template
        │       └── toolchain.template
        ├── __init__.py
        ├── log/
        │   └── gen_riscv.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_riscv_run.py

    6 directories, 18 files

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2021 - 2024 by `vroncevic.github.io/gen_riscv <https://vroncevic.github.io/gen_riscv>`_

**gen_riscv** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_riscv/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`