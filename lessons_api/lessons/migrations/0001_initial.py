# Generated by Django 3.0.1 on 2020-05-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('imageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
                ('startTime', models.CharField(max_length=10)),
                ('endTime', models.CharField(max_length=10)),
                ('weekDay', models.IntegerField()),
                ('appointment_id', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('pay', models.BooleanField()),
                ('appointment', models.BooleanField()),
                ('color', models.CharField(max_length=20)),
                ('availability', models.IntegerField()),
                ('teacher_v2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Teacher')),
            ],
        ),
    ]
