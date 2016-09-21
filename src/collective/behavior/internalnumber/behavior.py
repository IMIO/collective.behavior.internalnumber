# -*- coding: utf-8 -*-

from zope import component
from zope import schema
from zope.interface import alsoProvides, Invalid
from z3c.form import validator

from plone import api
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model

from Products.CMFPlone.utils import safe_unicode

from . import _
from browser.settings import get_pt_settings


class IInternalNumberBehavior(model.Schema):

    internal_number = schema.TextLine(
        title=_(u"Internal number"),
        required=False,)

alsoProvides(IInternalNumberBehavior, IFormFieldProvider)


def validateIndexValueUniqueness(context, portal_type, index_name, value):
    """
        check at 'portal_type' 'context' creation if 'index' 'value' is uniqueness
    """
    # if the value is empty, we don't check anything
    if not value:
        return
    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog.searchResults(**{index_name: value})
    if context.portal_type != portal_type:
        # we create the object, the context is the container
        if brains:
            raise Invalid(_(u"This value '${value}' is already used in ${obj}",
                            mapping={'obj': ', '.join(['<a href="%s" target="_blank">%s</a>' %
                                                       (safe_unicode(b.getURL()), safe_unicode(b.Title))
                                                       for b in brains]),
                                     'value': safe_unicode(value)}))
    else:
        # we edit the object, the context is itself
        # if multiple brains (normally not possible), we are sure there are other objects with same index value
        if len(brains) > 1 or (len(brains) == 1 and brains[0].UID != context.UID()):
            raise Invalid(_(u"This value '${value}' is already used in ${obj}",
                            mapping={'obj': ', '.join(['<a href="%s" target="_blank">%s</a>' %
                                                       (safe_unicode(b.getURL()), safe_unicode(b.Title))
                                                       for b in brains]),
                                     'value': safe_unicode(value)}))


class InternalNumberValidator(validator.SimpleFieldValidator):
    def validate(self, value):
        # we call the already defined validators
        # super(InternalNumberValidator, self).validate(value)
        if not get_pt_settings(self.view.portal_type).get('u', True):
            return
        validateIndexValueUniqueness(self.context, self.view.portal_type, 'internal_number', value)


validator.WidgetValidatorDiscriminators(InternalNumberValidator, field=IInternalNumberBehavior['internal_number'])
component.provideAdapter(InternalNumberValidator)
