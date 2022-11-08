# Generated by Django 4.1.1 on 2022-09-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_users',
            name='name',
        ),
        migrations.AlterField(
            model_name='custom_users',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
