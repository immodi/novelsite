# Generated by Django 4.1.5 on 2023-03-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0007_alter_novelmodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelmodel',
            name='cover',
            field=models.ImageField(upload_to='imgs'),
        ),
    ]
