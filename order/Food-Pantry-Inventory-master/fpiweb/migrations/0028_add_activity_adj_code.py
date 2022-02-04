# Generated by Django 3.0.5 on 2020-05-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpiweb', '0027_set_constraint_name_choices'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='adjustment_code',
            field=models.CharField(blank=True, choices=[('Fill Emptied', 'Fill emptied previous contents'), ('Move Added', 'Move added box'), ('Move Consumed', 'Move consumed the box'), ('Consume Added', 'Consume added box'), ('Consume Emptied', 'Consume emptied previous contents')], help_text='Coded reason if this entry was adjusted', max_length=15, null=True, verbose_name='Adjustment Code'),
        ),
    ]
