# Generated by Django 3.0.1 on 2019-12-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRNLabCore', '0002_auto_20191219_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]