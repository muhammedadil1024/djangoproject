# Generated by Django 4.1.2 on 2022-10-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regtable',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
