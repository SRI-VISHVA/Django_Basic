# Generated by Django 2.1.5 on 2019-02-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(default='+91', max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]