# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenRiscvBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_riscv.setup.keys import GenRiscvBundleKeys


class TestGenRiscvBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenRiscvBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenRiscvBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenRiscvBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenRiscvBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenRiscvBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenRiscvBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenRiscvBundleKeys.OPTION_INFO_FILE, opts)
