# Generated by Django 3.1.1 on 2020-10-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0008_poll_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optioncount',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='count', to='polling.option'),
        ),
    ]