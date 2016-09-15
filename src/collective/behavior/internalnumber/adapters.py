# -*- coding: utf-8 -*-

from plone.indexer import indexer
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone.utils import base_hasattr
from Products.PluginIndexes.common.UnIndex import _marker as common_marker


@indexer(IContentish)
def internal_number_index(obj):
    """ Index method escaping acquisition and ready for ZCatalog 3 """
    if base_hasattr(obj, 'internal_number') and obj.internal_number:
        return obj.internal_number
    return common_marker
