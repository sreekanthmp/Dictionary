# Generated by Django 4.1.3 on 2022-11-14 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0019_alter_dictionary_search_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='search_count',
            new_name='Dict',
        ),
    ]
