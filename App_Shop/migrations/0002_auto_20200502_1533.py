# Generated by Django 3.0.3 on 2020-05-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='minimage',
            new_name='mainimage',
        ),
    ]
