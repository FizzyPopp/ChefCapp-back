# Generated by Django 2.2.3 on 2019-08-18 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20190818_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='Ingredient Sub Size', max_length=256)),
            ],
            options={
                'db_table': 'subsize',
            },
        ),
        migrations.AddField(
            model_name='unitingredient',
            name='size',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='items.SubSize'),
        ),
    ]
