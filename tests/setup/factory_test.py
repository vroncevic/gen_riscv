# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenRiscvBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_riscv.setup.bundle import GenRiscvBundle
from gen_riscv.setup.factory import GenRiscvBundleFactory


class TestGenRiscvBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenRiscvBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenRiscvBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_riscv/infrastructure/config/gen_riscv.cfg'}
        bundle = GenRiscvBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenRiscvBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenRiscvBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenRiscvBundleFactory.get_version(), '1.0.5')
