# Generated by Django 3.2.7 on 2021-09-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='insturment',
            new_name='instrument',
        ),
    ]
