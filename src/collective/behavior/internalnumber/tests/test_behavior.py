# -*- coding: utf-8 -*-

import unittest

from zope.component import getUtility
from zope.interface import Invalid

from plone import api
from plone.dexterity.interfaces import IDexterityFTI

from collective.behavior.internalnumber.testing import COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING  # noqa

from ..behavior import validateIndexValueUniqueness


class TestBehavior(unittest.TestCase):
    """Test that collective.behavior.internalnumber is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.tt1 = self.portal['tt1']
        self.tt2 = api.content.create(container=self.portal, id='tt2', type='testtype', title='My content 2')
        self.tt2.reindexObject()

    def test_content(self):
        self.assertEqual(self.tt1.internal_number, 'AA123')
        self.assertEqual(self.tt2.internal_number, None)

    def test_index(self):
        pc = self.portal.portal_catalog
        brains = pc(portal_type='testtype')
        self.assertEqual(len(brains), 2)
        brains = pc(portal_type='testtype', internal_number='AA123')
        self.assertEqual(len(brains), 1)

    def test_searchabletext_index(self):
        fti = getUtility(IDexterityFTI, name='testtype')
        behaviors = list(fti.behaviors)
        behaviors.append('collective.dexteritytextindexer.behavior.IDexterityTextIndexer')
        fti._updateProperty('behaviors', tuple(behaviors))
        self.tt1.reindexObject()
        pc = self.portal.portal_catalog
        brains = pc(portal_type='testtype', SearchableText='AA123')
        self.assertEqual(len(brains), 1)

    def test_validator(self):
        self.assertRaises(Invalid, validateIndexValueUniqueness, self.tt2, 'testtype', 'internal_number', 'AA123')
        self.assertIsNone(validateIndexValueUniqueness(self.tt2, 'testtype', 'internal_number', 'AA1234'))
