# Generated by Django 4.1.5 on 2023-03-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0013_novelmodel_cover_alter_novelmodel_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelmodel',
            name='cover',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
