# Generated by Django 4.1.5 on 2023-03-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0011_novelmodel_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novelmodel',
            name='cover',
        ),
    ]