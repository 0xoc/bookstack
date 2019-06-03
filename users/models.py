from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models import signals
# Create your models here.


class UserProfile(models.Model):
    """
    every user is given a profile which is associated with a django user
    """

    user = models.OneToOneField(User, related_name="user_profile",
                                unique=True, verbose_name=_('Django User'),
                                help_text=_("Django User"), on_delete=models.CASCADE)

    avatar = models.ImageField(verbose_name=_("User's Avatar"),
                               help_text=_("Users's Avatar"),
                               blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(signals.post_save, sender=User)
def create_profile_for_user(sender, created, instance, **kwargs):
    """
    create a profile for every newly created django user
    """

    if created:
        UserProfile.objects.create(user=instance)