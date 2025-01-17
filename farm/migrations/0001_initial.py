# Generated by Django 5.0.1 on 2024-03-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('capability', models.CharField(blank=True, max_length=500)),
                ('host_tee', models.CharField(blank=True, max_length=100)),
                ('is_alive', models.BooleanField(default=False)),
                ('is_free', models.BooleanField(default=False)),
                ('last_used', models.DateTimeField(blank=True)),
                ('added_at', models.DateTimeField(blank=True)),
            ],
        ),
    ]
