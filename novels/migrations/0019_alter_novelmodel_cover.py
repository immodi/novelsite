# Generated by Django 4.1.5 on 2023-03-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0018_alter_novelmodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelmodel',
            name='cover',
            field=models.ImageField(default=None, max_length=10000, upload_to=''),
        ),
    ]
