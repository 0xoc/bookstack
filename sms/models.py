from django.db import models
from django.utils.translation import ugettext as _


class Receiver(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"),
                                    help_text=_("Receivers phone number"))


class Message(models.Model):
    to = models.ManyToManyField(Receiver, related_name="inbox", verbose_name=_("Recipients of the message"),
                                help_text=_("Recipients of the message"))
    message = models.CharField(max_length=500, verbose_name=_("Message Text"), help_text=_("Message Text"))

    block_code = models.IntegerField(blank=True, null=True, verbose_name=_("Block Code"), help_text=_("Block Code"))

    last_try = models.DateTimeField(blank=True, null=True)


class Operator(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Operator Name"), help_text=_("A name for the operator"))

    username = models.CharField(max_length=255, verbose_name=_("Username"), help_text=_("User name given by operator"))
    password = models.CharField(max_length=255, verbose_name=_("Password"), help_text=_("Password given by operator"))

    sender = models.CharField(max_length=15, verbose_name=_("Sender Phone Number"),
                              help_text=_("The operator phone number"))

    retry_gap_time = models.IntegerField(verbose_name=_("Retry Gap Time"),
                                         help_text=_("Time in minutes before you can try to send a message again"))






