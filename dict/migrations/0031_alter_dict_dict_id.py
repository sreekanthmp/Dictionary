# Generated by Django 4.1.3 on 2022-11-14 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0030_remove_dictionary_dict_id_alter_dict_dict_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='dict_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dictId', to='dict.dictionary'),
        ),
    ]
