from django.apps import AppConfig
from django.utils.translation import ugettext as _


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = _('Users')
