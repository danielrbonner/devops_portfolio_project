# Generated by Django 3.2.2 on 2022-01-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundles', '0002_bundle_programs'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bundles',
            field=models.ManyToManyField(to='bundles.Bundle'),
        ),
    ]
