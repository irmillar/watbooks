# Generated by Django 2.1.7 on 2020-03-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200321_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FA', 'Fantasy'), ('SF', 'Science Fiction'), ('RO', 'Romance'), ('TH', 'Thriller'), ('MY', 'Mystery'), ('DY', 'Dystopia'), ('SS', 'Short Story'), ('SU', 'Surrealism'), ('SC', 'Science'), ('EC', 'Economics'), ('MA', 'Maths'), ('HI', 'History'), ('PH', 'Philosophy'), ('FI', 'Finance'), ('OT', 'Other')], max_length=20),
        ),
    ]
