# Generated by Django 3.0.2 on 2020-06-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mailer_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailer',
            name='subject',
            field=models.CharField(default='no subject', max_length=254),
        ),
    ]
