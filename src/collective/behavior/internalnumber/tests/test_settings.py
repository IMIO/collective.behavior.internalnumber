# -*- coding: utf-8 -*-

import unittest

from plone import api

from collective.behavior.internalnumber.testing import COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING  # noqa

from .. import TYPE_CONFIG
from ..browser.settings import get_settings, get_pt_settings, DxPortalTypesVocabulary


class TestSettings(unittest.TestCase):
    """Test settings."""

    layer = COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.tt1 = self.portal['tt1']
        api.portal.set_registry_record(TYPE_CONFIG, [{u'portal_type': u'glo_bal', u'uniqueness': False},
                                                     {u'portal_type': u'testtype', u'uniqueness': True}])

    def test_get_settings(self):
        self.assertDictEqual(get_settings(), {u'glo_bal': {u'u': False}, u'testtype': {u'u': True}})

    def test_get_pt_settings(self):
        self.assertDictEqual(get_pt_settings('testtype'), {u'u': True})
        api.portal.set_registry_record(TYPE_CONFIG, [{u'portal_type': u'glo_bal', u'uniqueness': False}])
        self.assertDictEqual(get_pt_settings('testtype'), {u'u': False})

    def test_DxPortalTypesVocabulary(self):
        voc_inst = DxPortalTypesVocabulary()
        voc_list = [(t.value, t.title) for t in voc_inst(self.portal)]
        self.assertEqual(voc_list, [('glo_bal', u'Global configuration'), ('testtype', u'Test type')])
