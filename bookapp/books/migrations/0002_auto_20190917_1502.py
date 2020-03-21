# Generated by Django 2.1.7 on 2019-09-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.CharField(choices=[('FA', 'Fantasy'), ('SF', 'Science Fiction'), ('RO', 'Romance'), ('TH', 'Thriller'), ('MY', 'Mystery'), ('DY', 'Dystopia'), ('SS', 'Short Story'), ('SU', 'Surrealism'), ('SC', 'Science'), ('EC', 'Economics'), ('MA', 'Maths'), ('HI', 'History'), ('OT', 'Other')], max_length=20),
        ),
    ]