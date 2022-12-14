# Generated by Django 4.1.1 on 2022-11-23 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0011_alumnidata_announcements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund_Raise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('amount', models.CharField(max_length=256)),
                ('account_no', models.CharField(max_length=256)),
                ('bank_name', models.CharField(max_length=256)),
                ('custom_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
