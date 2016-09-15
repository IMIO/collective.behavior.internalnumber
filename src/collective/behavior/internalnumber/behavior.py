# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import alsoProvides

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model

from . import _


class IInternalNumberBehavior(model.Schema):

    internal_number = schema.TextLine(
        title=_(u"Internal Reference Number"),
        required=False,)

alsoProvides(IInternalNumberBehavior, IFormFieldProvider)
