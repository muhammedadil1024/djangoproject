# Generated by Django 4.1.2 on 2022-10-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
    ]
