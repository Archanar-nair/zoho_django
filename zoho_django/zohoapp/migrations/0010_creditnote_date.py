# Generated by Django 3.2.18 on 2023-05-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_auto_20230429_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnote',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
