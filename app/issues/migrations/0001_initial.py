# Generated by Django 3.2.2 on 2022-01-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_description', models.CharField(default='', max_length=250)),
                ('notes', models.CharField(default='', max_length=400)),
                ('issue_create_date', models.DateField()),
                ('issue_due_date', models.DateField()),
                ('program_id', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
