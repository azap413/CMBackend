# Generated by Django 3.0.5 on 2021-06-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0004_auto_20210612_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='lata',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
        migrations.AlterField(
            model_name='ride',
            name='latb',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
        migrations.AlterField(
            model_name='ride',
            name='longa',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
        migrations.AlterField(
            model_name='ride',
            name='longb',
            field=models.DecimalField(decimal_places=20, max_digits=50),
        ),
    ]