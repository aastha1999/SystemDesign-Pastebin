# Generated by Django 3.2.11 on 2022-01-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]
