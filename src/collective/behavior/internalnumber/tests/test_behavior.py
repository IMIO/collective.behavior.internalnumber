# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.behavior.internalnumber.testing import COLLECTIVE_BEHAVIOR_INTERNALNUMBER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


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
