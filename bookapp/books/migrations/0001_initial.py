# Generated by Django 2.1.7 on 2019-09-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('isbn', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('added_date', models.DateField(blank=True, null=True)),
                ('borrowed_to', models.CharField(blank=True, max_length=200, null=True)),
                ('genres', models.CharField(max_length=20)),
                ('book_type', models.CharField(choices=[('FI', 'Fiction'), ('NF', 'Non-Fiction')], max_length=40, verbose_name='Fiction or Non-Fiction')),
            ],
        ),
    ]