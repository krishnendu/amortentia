# Generated by Django 3.0.3 on 2020-02-10 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousclass',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='text time'),
            preserve_default=False,
        ),
    ]
