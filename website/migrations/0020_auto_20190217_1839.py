# Generated by Django 2.0.9 on 2019-02-17 07:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20190217_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tesimonial',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
