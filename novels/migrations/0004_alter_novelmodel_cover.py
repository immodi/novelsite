# Generated by Django 4.1.5 on 2023-03-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0003_novelmodel_cover_novelmodel_info_novelmodel_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelmodel',
            name='cover',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
