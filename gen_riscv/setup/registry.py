# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_riscv components for simplification of gen_riscv bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_riscv.core.service.iservice import IService
from gen_riscv.core.service.isubprocessor import ISubProcessor
from gen_riscv.infrastructure.cli.icli import ICLI
from gen_riscv.setup.bundle import GenRiscvBundle
from gen_riscv.setup.validator import GenRiscvBundleValidator
from gen_riscv.setup.keys import GenRiscvBundleKeys
from gen_riscv.setup.dependencies import GenRiscvBundleDependencies
from gen_riscv.setup.dep_validator import GenRiscvBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_riscv'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_riscv/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRiscvBundleRegistry:
    '''
        Encapsulates core gen_riscv components for simplification of gen_riscv bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_riscv bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenRiscvBundleDependencies) -> GenRiscvBundle:
        '''
            Creates the gen_riscv bundle.

            :param dependencies: The gen_riscv bundle dependencies.
            :return: The gen_riscv bundle.
            :exceptions:
                | ATSValueError: The gen_riscv bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_riscv bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_riscv bundle must be provided and have proper values.
                | ATSTypeError:  The gen_riscv bundle must be an instance of GenRiscvBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenRiscvBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenRiscvBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenRiscvBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenRiscvBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenRiscvBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenRiscvBundle = GenRiscvBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenRiscvBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
