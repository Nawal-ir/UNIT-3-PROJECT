# Generated by Django 5.0.3 on 2024-04-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_recipe_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_estimate',
            field=models.CharField(max_length=100),
        ),
    ]
