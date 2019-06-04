from django.contrib import admin
from .models import *


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['text', 'classification']
    list_display_links = ['text', 'classification']
    list_filter = ['classification__text', ]


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ['text', 'count']
    list_display_links = ['text', ]


admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Tag, TagAdmin)
