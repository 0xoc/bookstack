from django.contrib import admin

# Register your models here.
from .models import *


class YesNoQuestionInline(admin.TabularInline):
    model = YesNoQuestion
    fields = ['text', 'is_ticked']
    readonly_fields = ['text', 'is_ticked']


class MultipleChoiceQuestionInline(admin.TabularInline):
    model = MultipleChoiceQuestion
    fields = ['text', 'is_single_choice',]
    readonly_fields = ['text', 'is_single_choice']


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['text', 'is_selected']
    readonly_fields = ['text', 'is_selected']


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ['title', ]
    inlines = [
        YesNoQuestionInline,
        MultipleChoiceQuestionInline,
    ]


class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_single_choice', 'question']
    list_display_links = ['text', 'question']
    # list
    inlines = [AnswerInline, ]


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(YesNoQuestion)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(Answer)
