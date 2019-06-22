from django.contrib import admin, messages
from django import forms
from django.shortcuts import get_object_or_404

from .models import *
# Register your models here.
from django.contrib.admin.helpers import ActionForm
from django.utils.translation import ugettext as _


class SendMessageForm(ActionForm):
    operator = forms.ModelChoiceField(queryset=Operator.objects.all())


def send_message_action(self, request, queryset):
    operator = request.POST['operator']
    operator = get_object_or_404(Operator, pk=operator)

    count = 0

    for message in queryset:
        response = operator.send_message(message)

        if response['status'] == 'OK':
            count += 1
        else:
            messages.error(request, 'Message Not sent')

    messages.success(request, '%d messages sent' % (count,))


send_message_action.short_description = _("Send Message")


class MessageAdmin(admin.ModelAdmin):
    action_form = SendMessageForm
    list_display = ['to', 'message', 'block_code']
    actions = [send_message_action, ]


admin.site.register(Message, MessageAdmin)
admin.site.register(Operator)
