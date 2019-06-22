from django.db import models
from django.utils.translation import ugettext as _


class Receiver(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"),
                                    help_text=_("Receivers phone number"))


class Message(models.Model):
    sender = models.CharField(max_length=15, verbose_name=_("Sender"), help_text=_("Senders Phone number"))
    operator = models.CharField(max_length=15, verbose_name=_("From"), help_text=_("The operator to send the sms from"))
    to = models.ManyToManyField(Receiver, related_name="inbox", verbose_name=_("Recipients of the message"),
                                help_text=_("Recipients of the message"))
    message = models.CharField(max_length=500, verbose_name=_("Message Text"), help_text=_("Message Text"))

    block_code = models.IntegerField(blank=True, null=True, verbose_name=_("Block Code"), help_text=_("Block Code"))

    last_try = models.DateTimeField(auto_now=True)





