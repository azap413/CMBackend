# Generated by Django 3.0.5 on 2021-05-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
