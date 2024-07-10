# -*- coding: UTF-8 -*-

'''
Module
    gen_riscv_test.py
Copyright
    Copyright (C) 2021 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class TestGenRISCV with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenRISCV.
Execute
    python3 -m unittest -v gen_riscv_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from gen_riscv import GenRISCV
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_riscv'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_riscv/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenRISCV(TestCase):
    '''
        Defines class TestGenRISCV with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenRISCV.
        GenRISCV unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_process_tool - Test generation of tool structure.
    '''
    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenRISCV = GenRISCV()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: GenRISCV = GenRISCV()
        self.assertFalse(generator.process())

    def test_process_tool(self) -> None:
        '''Test generation of my project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'mypro')
        generator: GenRISCV = GenRISCV()
        self.assertTrue(generator.process())


if __name__ == '__main__':
    main()
