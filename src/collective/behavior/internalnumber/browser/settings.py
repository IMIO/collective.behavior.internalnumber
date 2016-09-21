from zope import schema
from zope.interface import Interface
from z3c.form import form

from plone import api
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.autoform.directives import widget
from plone.z3cform import layout

from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow

from .. import _, TYPE_CONFIG


class IPortalTypeConfigSchema(Interface):
    portal_type = schema.TextLine(title=_("Portal type"), required=True)
    uniqueness = schema.Bool(title=_("Uniqueness"), required=False)


class IInternalNumberConfig(Interface):
    """
    Configuration of internalnumber
    """

    portal_type_config = schema.List(
        title=_(u'By type configuration'),
#        description=_(u"Useless description."),
        value_type=DictRow(title=_("Portal type conf"),
                           schema=IPortalTypeConfigSchema))

    widget('portal_type_config', DataGridFieldFactory)


class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    form.extends(RegistryEditForm)
    schema = IInternalNumberConfig
    label = _("Internal number behavior configuration")

SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)


def get_settings():
    ptc = api.portal.get_registry_record(TYPE_CONFIG)
    settings = {}
    if ptc is None:
        return settings
    for row in ptc:
        settings[row['portal_type']] = {'u': row['uniqueness']}
    return settings


def get_pt_settings(pt):
    settings = get_settings()
    if pt not in settings:
        return {}
    return settings[pt]
