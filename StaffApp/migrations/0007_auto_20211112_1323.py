# Generated by Django 3.2.8 on 2021-11-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaffApp', '0006_auto_20211112_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrequest',
            name='Status',
        ),
        migrations.AddField(
            model_name='offersrequest',
            name='Status',
            field=models.IntegerField(null=True),
        ),
    ]