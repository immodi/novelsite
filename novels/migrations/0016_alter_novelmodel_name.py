# Generated by Django 4.1.5 on 2023-03-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0015_alter_novelmodel_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelmodel',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
