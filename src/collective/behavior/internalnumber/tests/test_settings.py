# -*- coding: utf-8 -*-

import unittest

from plone import api

from collective.behavior.internalnumber.testing import COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING  # noqa

from .. import TYPE_CONFIG
from ..browser.settings import get_settings, get_pt_settings


class TestSettings(unittest.TestCase):
    """Test settings."""

    layer = COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.tt1 = self.portal['tt1']
        api.portal.set_registry_record(TYPE_CONFIG, [{u'portal_type': u'testtype', u'uniqueness': True}])

    def test_get_settings(self):
        self.assertDictEqual(get_settings(), {u'testtype': {u'u': True}})

    def test_get_pt_settings(self):
        self.assertDictEqual(get_pt_settings('testtype'), {u'u': True})
