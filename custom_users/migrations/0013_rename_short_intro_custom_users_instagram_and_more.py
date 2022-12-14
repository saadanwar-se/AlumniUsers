# Generated by Django 4.1.1 on 2022-11-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0012_fund_raise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custom_users',
            old_name='short_intro',
            new_name='instagram',
        ),
        migrations.RemoveField(
            model_name='custom_users',
            name='is_alumni',
        ),
        migrations.RemoveField(
            model_name='custom_users',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='custom_users',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custom_users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='custom_users',
            name='picture',
            field=models.ImageField(default='', upload_to='my_picture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='custom_users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
