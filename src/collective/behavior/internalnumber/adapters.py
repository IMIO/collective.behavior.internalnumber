# -*- coding: utf-8 -*-

from collective.behavior.internalnumber.behavior import IInternalNumberBehavior
from collective.dexteritytextindexer.interfaces import IDynamicTextIndexExtender
from plone.indexer import indexer
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone.utils import base_hasattr
from Products.CMFPlone.utils import safe_unicode
from Products.PluginIndexes.common.UnIndex import _marker as common_marker
from zope.component import adapts
from zope.interface import implements


@indexer(IContentish)
def internal_number_index(obj):
    """ Index method escaping acquisition and ready for ZCatalog 3 """
    if base_hasattr(obj, 'internal_number') and obj.internal_number:
        return obj.internal_number
    return common_marker


class InternalNumberSearchableExtender(object):
    """
        Extends SearchableText of IInternalNumberBehavior objects.
    """
    adapts(IInternalNumberBehavior)
    implements(IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        return safe_unicode(self.context.internal_number)
