# Generated by Django 4.0.4 on 2022-06-06 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogLogin', '0004_userblog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserBlog',
        ),
    ]
