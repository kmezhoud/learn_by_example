# Generated by Django 2.1.7 on 2019-04-20 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpiweb', '0012_auto_20190419_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Activity',
            old_name='box_type_code',
            new_name='box_type',
        ),
        migrations.RenameField(
            model_name='Activity',
            old_name='expiration_month_end',
            new_name='exp_month_end',
        ),
        migrations.RenameField(
            model_name='Activity',
            old_name='expiration_year',
            new_name='exp_year',
        ),
        migrations.RenameField(
            model_name='Activity',
            old_name='expiration_month_start',
            new_name='exp_month_start',
        ),
    ]