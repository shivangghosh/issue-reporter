# Generated by Django 3.1.1 on 2020-09-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_auto_20200910_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]