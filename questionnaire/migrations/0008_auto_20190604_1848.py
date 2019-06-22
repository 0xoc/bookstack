# Generated by Django 2.2.1 on 2019-06-04 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_auto_20190604_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'جواب', 'verbose_name_plural': 'جواب ها'},
        ),
        migrations.AlterModelOptions(
            name='descriptivequestion',
            options={'verbose_name': 'سوال تشریحی', 'verbose_name_plural': 'سوال های تشریحی'},
        ),
        migrations.AlterModelOptions(
            name='multiplechoicequestion',
            options={'verbose_name': 'سوال چند جوابی', 'verbose_name_plural': 'سوال های چند جوابی'},
        ),
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': 'پرسشنامه', 'verbose_name_plural': 'پرسشنامه ها'},
        ),
        migrations.AlterModelOptions(
            name='yesnoquestion',
            options={'verbose_name': 'سوال بله یا خیر', 'verbose_name_plural': 'سوای های بله یا خیر'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_selected',
            field=models.BooleanField(default=False, help_text='آیا جواب انتخاب شده', verbose_name='انتخاب شده'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='multiple_choice_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='questionnaire.MultipleChoiceQuestion', verbose_name='جواب سوال چندجوابی'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(help_text='عنوان', max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='descriptivequestion',
            name='description',
            field=models.TextField(blank=True, help_text='توضیح سوال', max_length=1000, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='descriptivequestion',
            name='question',
            field=models.ForeignKey(help_text='پرسشنامه سوال تشریحی', on_delete=django.db.models.deletion.CASCADE, related_name='descriptive_question', to='questionnaire.Questionnaire', verbose_name='پرسشنامه ها'),
        ),
        migrations.AlterField(
            model_name='descriptivequestion',
            name='text',
            field=models.CharField(help_text='عنوان', max_length=255, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='is_single_choice',
            field=models.BooleanField(help_text='آیا تک انتخابی است؟', verbose_name='آیا تک انتخابی است؟'),
        ),
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='question',
            field=models.ForeignKey(help_text='پرسشنامه سوال چند جوابی', on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_question', to='questionnaire.Questionnaire', verbose_name='پرسشنامه ها'),
        ),
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='text',
            field=models.CharField(help_text='عنوان', max_length=255, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='text',
            field=models.CharField(help_text='عنوان پرسشنامه', max_length=255, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='yesnoquestion',
            name='is_ticked',
            field=models.BooleanField(default=False, help_text='آیا انتخاب شده؟', verbose_name='انتخاب شده؟'),
        ),
        migrations.AlterField(
            model_name='yesnoquestion',
            name='question',
            field=models.ForeignKey(help_text='پرسشنامه ی سوال بله یا خیر', on_delete=django.db.models.deletion.CASCADE, related_name='yes_no_question', to='questionnaire.Questionnaire', verbose_name='پرسشنامه ها'),
        ),
        migrations.AlterField(
            model_name='yesnoquestion',
            name='text',
            field=models.CharField(help_text='عنوان سوال', max_length=255, verbose_name='عنوان'),
        ),
    ]