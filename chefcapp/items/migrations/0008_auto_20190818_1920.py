# Generated by Django 2.2.3 on 2019-08-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20190818_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]