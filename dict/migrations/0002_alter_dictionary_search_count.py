# Generated by Django 4.1.3 on 2022-11-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='search_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
