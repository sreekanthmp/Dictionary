# Generated by Django 4.1.3 on 2022-11-14 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0026_alter_dictionary_search_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictionary',
            name='search_count',
        ),
        migrations.AddField(
            model_name='dict',
            name='dict_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Id', to='dict.dictionary'),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='dict_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]