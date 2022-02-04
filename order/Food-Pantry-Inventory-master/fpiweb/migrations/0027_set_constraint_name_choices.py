# Generated by Django 2.2.10 on 2020-02-23 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpiweb', '0026_auto_20200210_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constraints',
            name='constraint_name',
            field=models.CharField(choices=[('Row', 'Rows in the warehouse'), ('Bin', 'Bins in the Warehouse'), ('Tier', 'Tiers in the Warehouse'), ('Location Exclusions ', 'Warehouse locations excluded from inventory'), ('Quantity Limit', 'Typical count of items in a box'), ('Future Expiration Year Limit', 'Maximum years of future expiration permitted')], help_text='Coded name of a constraint.', max_length=30, unique=True, verbose_name='Constraint Name'),
        ),
    ]
