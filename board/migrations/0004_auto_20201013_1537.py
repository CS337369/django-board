# Generated by Django 3.1.2 on 2020-10-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20201013_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_note',
            field=models.TextField(help_text='내용을 입력하세요.', null=True),
        ),
    ]
