# Generated by Django 4.2 on 2023-05-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_code', models.CharField(max_length=50)),
                ('c_name', models.CharField(max_length=255)),
                ('c_des', models.CharField(max_length=255)),
                ('c_du', models.CharField(max_length=200)),
                ('c_fee', models.IntegerField()),
            ],
        ),
    ]