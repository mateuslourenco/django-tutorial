# Generated by Django 3.2.7 on 2021-10-03 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
