# Generated by Django 4.1.3 on 2022-11-13 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0009_alter_dictionary_dict_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='dict_id',
            new_name='search_count',
        ),
        migrations.DeleteModel(
            name='DictCount',
        ),
    ]
