from django.apps import AppConfig
from django.utils.translation import ugettext as _


class QuestionnaireConfig(AppConfig):
    name = 'questionnaire'
    verbose_name = _('Questionnaire')
