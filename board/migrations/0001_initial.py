# Generated by Django 3.1.2 on 2020-10-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.AutoField(primary_key=True, serialize=False)),
                ('b_title', models.CharField(max_length=255)),
                ('b_note', models.TextField(null=True)),
                ('b_writer', models.CharField(max_length=50)),
                ('parent_no', models.IntegerField(default=0, null=True)),
                ('b_count', models.IntegerField(default=0)),
                ('b_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('usage_flag', models.CharField(default='1', max_length=10)),
            ],
        ),
    ]
