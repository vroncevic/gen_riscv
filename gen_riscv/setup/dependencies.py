# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_riscv is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_riscv is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    GenRiscv bundle dependencies for the gen_riscv bundle.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.base.setup.bundle import BaseBundle

from gen_riscv.core.service.iservice import IService
from gen_riscv.core.service.isubprocessor import ISubProcessor
from gen_riscv.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_riscv'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_riscv/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRiscvBundleDependencies(TypedDict):
    '''
        GenRiscv bundle dependencies for the gen_riscv bundle.

        It defines:

            :attributes:
                | base - The base bundle with the base components for the gen_riscv bundle.
                | service - The service orchestrating the gen_riscv's execution for the gen_riscv bundle.
                | subprocessor - The adapter executing the gen_riscv's sub-processes for the gen_riscv bundle.
                | cli - The command-line interface adapter for the gen_riscv bundle.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI
