# Generated by Django 4.1.1 on 2022-10-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0009_custom_users_company_name_custom_users_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_users',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='custom_users',
            name='designation',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='custom_users',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('TEACHER', 'TEACHER'), ('STUDENT', 'STUDENT'), ('ALUMNI', 'ALUMNI')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='custom_users',
            name='uuid',
            field=models.CharField(blank=True, editable=False, max_length=13, null=True, unique=True),
        ),
    ]