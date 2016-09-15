# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.behavior.internalnumber.testing import COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.internalnumber is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.internalnumber is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.behavior.internalnumber'))

    def test_browserlayer(self):
        """Test that ICollectiveBehaviorInternalnumberLayer is registered."""
        from collective.behavior.internalnumber.interfaces import (
            ICollectiveBehaviorInternalnumberLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveBehaviorInternalnumberLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.behavior.internalnumber'])

    def test_product_uninstalled(self):
        """Test if collective.behavior.internalnumber is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.behavior.internalnumber'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveBehaviorInternalnumberLayer is removed."""
        from collective.behavior.internalnumber.interfaces import ICollectiveBehaviorInternalnumberLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveBehaviorInternalnumberLayer, utils.registered_layers())
