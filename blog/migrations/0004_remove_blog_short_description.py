# Generated by Django 4.2.7 on 2023-11-10 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='short_description',
        ),
    ]
