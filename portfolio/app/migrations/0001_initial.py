# Generated by Django 5.1.5 on 2025-02-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='static/img')),
                ('date', models.IntegerField()),
            ],
        ),
    ]
