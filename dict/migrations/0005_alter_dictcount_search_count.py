# Generated by Django 4.1.3 on 2022-11-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_alter_dictionary_search_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictcount',
            name='search_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]