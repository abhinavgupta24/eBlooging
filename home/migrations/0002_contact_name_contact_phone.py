# Generated by Django 4.2 on 2023-05-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="name",
            field=models.CharField(blank=True, max_length=122),
        ),
        migrations.AddField(
            model_name="contact",
            name="phone",
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
