# Generated by Django 3.1.2 on 2020-10-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='a_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]