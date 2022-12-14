# Generated by Django 4.1.3 on 2022-11-13 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0005_alter_dictcount_search_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictcount',
            name='search_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='search_count',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Search_count', to='dict.dictcount'),
        ),
    ]
