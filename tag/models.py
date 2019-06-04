from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.

class Classification(models.Model):
    """
        classifications of tags.
    """

    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')

    text = models.CharField(max_length=255, verbose_name=_('text'), help_text=_('text for a classification of tags.'))


class Tag(models.Model):
    """
        tags for objects.
    """

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    text = models.CharField(max_length=255, verbose_name=_('text'), help_text=_('text for tag'))
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, verbose_name=_('classification'),
                                       related_name='tag', help_text=_('classification for a tag'))
