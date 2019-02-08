# Generated by Django 2.0.9 on 2019-02-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190207_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
