# Generated by Django 4.1.3 on 2022-11-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0012_dictionary_search_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_count', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='search_count',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Count', to='dict.dictcount'),
        ),
    ]
