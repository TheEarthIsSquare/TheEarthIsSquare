# Generated by Django 2.0.9 on 2019-02-09 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190209_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='parent_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Service'),
        ),
    ]