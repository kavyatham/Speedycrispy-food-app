# Generated by Django 2.1.7 on 2020-06-27 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('restro_id', models.AutoField(primary_key=True, serialize=False)),
                ('restro_name', models.CharField(max_length=30, unique=True)),
                ('restro_contact', models.IntegerField(unique=True)),
                ('restro_email', models.EmailField(max_length=100, unique=True)),
                ('restro_password', models.CharField(max_length=30)),
                ('restro_otp', models.IntegerField()),
                ('restro_status', models.CharField(default=False, max_length=30)),
                ('restro_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.AreaModel')),
                ('restro_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.RestaurantTypeModel')),
            ],
        ),
    ]
