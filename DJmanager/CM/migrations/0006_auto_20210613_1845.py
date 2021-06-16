# Generated by Django 3.0.5 on 2021-06-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0005_auto_20210613_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='currentlocation',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='destination',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='latb',
            field=models.DecimalField(decimal_places=20, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='longb',
            field=models.DecimalField(decimal_places=20, max_digits=50, null=True),
        ),
    ]