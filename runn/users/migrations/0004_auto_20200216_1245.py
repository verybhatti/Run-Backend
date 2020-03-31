# Generated by Django 2.2 on 2020-02-16 12:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200216_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='anas', editable=False, populate_from=['first_name', 'last_name'], unique=True),
            preserve_default=False,
        ),
    ]