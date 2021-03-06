# Generated by Django 3.2.2 on 2022-01-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_id', models.CharField(default='', max_length=20)),
                ('program_name', models.CharField(default='', max_length=200)),
                ('program_type', models.CharField(blank=True, max_length=50, null=True)),
                ('retailer', models.CharField(blank=True, max_length=50)),
                ('retailer_item_nbr', models.CharField(blank=True, max_length=20)),
                ('program_UPC', models.CharField(blank=True, max_length=20)),
                ('season', models.CharField(blank=True, max_length=20)),
                ('year', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
