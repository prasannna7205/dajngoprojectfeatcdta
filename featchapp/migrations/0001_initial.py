# Generated by Django 4.1.4 on 2023-02-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('eno', models.IntegerField()),
                ('esal', models.IntegerField()),
                ('addrs', models.CharField(max_length=100)),
            ],
        ),
    ]
