# Generated by Django 2.2.3 on 2019-08-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carstation', '0004_auto_20190730_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carstation',
            name='bookings',
            field=models.IntegerField(default=0),
        ),
    ]
