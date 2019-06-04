from django.apps import AppConfig
from django.utils.translation import ugettext as _


class TagConfig(AppConfig):
    name = 'tag'
    verbose_name = _('Tag')
