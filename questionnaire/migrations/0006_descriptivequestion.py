# Generated by Django 2.2.1 on 2019-06-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_auto_20190603_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='text for descriptive question', max_length=255, verbose_name='text')),
                ('description', models.TextField(blank=True, help_text='Description for the asked question', max_length=1000, null=True, verbose_name='Description')),
                ('question', models.ForeignKey(help_text='questionnaire of descriptive question', on_delete=django.db.models.deletion.CASCADE, related_name='descriptive_question', to='questionnaire.Questionnaire', verbose_name='questionnaire')),
            ],
        ),
    ]