# Generated by Django 4.1.5 on 2023-04-11 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0025_remove_novelmodel_cover_novelmodel_cover_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='novelmodel',
            name='last_edited',
            field=models.CharField(db_index=True, default=0, max_length=1000),
        ),
    ]