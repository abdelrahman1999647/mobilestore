# Generated by Django 4.0.4 on 2022-05-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_cartorderitems_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='number',
            field=models.IntegerField(),
        ),
    ]
