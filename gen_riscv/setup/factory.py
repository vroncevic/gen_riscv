# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_riscv bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_riscv.setup.bundle import GenRiscvBundle
from gen_riscv.setup.options import GenRiscvBundleOptions
from gen_riscv.setup.registry import GenRiscvBundleRegistry
from gen_riscv.setup.dependencies import GenRiscvBundleDependencies
from gen_riscv.setup.opt_validator import GenRiscvBundleOptionsValidator
from gen_riscv.setup.keys import GenRiscvBundleKeys
from gen_riscv.core.service.engine import Service
from gen_riscv.infrastructure.subprocessor import SubProcessor
from gen_riscv.infrastructure.cli.engine import CLI
from gen_riscv.infrastructure.cli.setup.bundle import CLIBundle
from gen_riscv.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_riscv.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_riscv.infrastructure.command.command import CommandBundle
from gen_riscv.infrastructure.command.gen_riscv_command_definition import GenRiscvCommandDefinition
from gen_riscv.infrastructure.command.gen_riscv_command_executor import GenRiscvCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_riscv'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_riscv/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenRiscvBundleFactory:
    '''
        Factory for creating the gen_riscv bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_riscv info file.
            :methods:
                | create_bundle - Creates the gen_riscv bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = 'gen_riscv/infrastructure/config/gen_riscv.cfg'

    @classmethod
    def create_bundle(cls, options: GenRiscvBundleOptions | None = None) -> GenRiscvBundle:
        '''
            Creates the gen_riscv bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_riscv bundle.
            :return: The gen_riscv bundle.
            :exceptions:
                | ATSValueError: The gen_riscv bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_riscv bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_riscv bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_riscv bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_riscv bundle must be provided and have proper values.
                | ATSTypeError:  The gen_riscv bundle must be an instance of GenRiscvBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenRiscvBundleOptionsValidator.validate(options)

        info_file = options.get(GenRiscvBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_riscv_definition: GenRiscvCommandDefinition = GenRiscvCommandDefinition()

        gen_riscv_bundle: CommandBundle = CommandBundle(
            definition=gen_riscv_definition,
            executor=GenRiscvCommandExecutor(gen_riscv_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_riscv_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenRiscvBundleRegistry.create_bundle(
            dependencies=GenRiscvBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
