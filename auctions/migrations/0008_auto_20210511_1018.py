# Generated by Django 2.2 on 2021-05-11 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
