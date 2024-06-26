# Generated by Django 5.0.4 on 2024-05-21 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_school', '0003_course_owner_lesson_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите автора курса', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор курса'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите автора урока', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор урока'),
        ),
    ]
