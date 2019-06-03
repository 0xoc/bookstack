from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.


class Questionnaire(models.Model):
    """
        the question title
    """

    class Meta:
        verbose_name = _('Questionnaire')
        verbose_name_plural = _('Questionnaires')

    text = models.CharField(max_length=255, verbose_name=_('title'), help_text=_('title for Questionnaire'))

    # has yes_no_question.all()
    # has multiple_choice_question.all()

    def add_question(self, text, answers=[], is_single_choice=False):

        # if is a yes no question
        if not answers:
            YesNoQuestion.objects.create(text=text, question=self)

        # if it's a multiple choice
        else:
            tmp_mcq = MultipleChoiceQuestion.objects.create(text=text, is_single_choice=is_single_choice, question=self)

            for answer in answers:
                Answer.objects.create(text=answer, multiple_choice_question=tmp_mcq)

    def __str__(self):
        return self.title


class YesNoQuestion(models.Model):
    """
        True/False questions
    """

    class Meta:
        verbose_name = _('Yes No Question')
        verbose_name_plural = _('Yes No Questions')

    text = models.CharField(max_length=255, verbose_name=_('text'), help_text=_('text of the yes no question'))
    is_ticked = models.BooleanField(default=False, verbose_name=_('is ticked'),
                                    help_text=_('is ticked for yes or no questions'))
    question = models.ForeignKey(Questionnaire, related_name="yes_no_question", on_delete=models.CASCADE,
                                 verbose_name=_('questionnaire'), help_text=_('questionnaire of yes no question'))

    def __str__(self):
        return self.text


class MultipleChoiceQuestion(models.Model):
    """
        questions which have more than one answer or one answer in many choices!
    """

    class Meta:
        verbose_name = _('Multiple Choice Question')
        verbose_name_plural = _('Multiple Choice Questions')

    question = models.ForeignKey(Questionnaire, related_name="multiple_choice_question",
                                 on_delete=models.CASCADE, verbose_name=_('questionnaire'),
                                 help_text=_('questionnaire of multiple choice question'))
    text = models.CharField(max_length=255, verbose_name=_('text'), help_text=_('text for multiple choice question'))
    is_single_choice = models.BooleanField(verbose_name=_('is single choice'),
                                           help_text=_('is single choice for multiple choice questions'))

    # has answer.all()

    def __str__(self):
        return self.text


class Answer(models.Model):
    """
        the choices to the MultipleChoiceQuestion model questions
    """

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    text = models.CharField(max_length=100, verbose_name=_('text'),
                            help_text=_('text for answer of multiple choice questions'))
    is_selected = models.BooleanField(default=False, verbose_name=_('is selected'),
                                      help_text=_('is an answer selected or not'))
    multiple_choice_question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE,
                                                 related_name='answer',
                                                 verbose_name=_('answer for multiple choice questions'))

    def __str__(self):
        return self.text
