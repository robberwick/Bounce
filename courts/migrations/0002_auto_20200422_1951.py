# Generated by Django 2.0 on 2020-04-23 00:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapAPIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('api_key', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='court',
            name='id',
            field=models.CharField(default=uuid.UUID('7ef27bb3-a536-4e93-83c7-11b6d7b06dd4'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]