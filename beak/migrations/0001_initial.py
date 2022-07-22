# Generated by Django 4.0.5 on 2022-07-22 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('google_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('google_rating', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recommended_places', models.ManyToManyField(to='beak.place')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('number', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('places', models.ManyToManyField(blank=True, to='beak.place')),
            ],
        ),
        migrations.CreateModel(
            name='General_Location',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('places', models.ManyToManyField(blank=True, to='beak.place')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beak.place')),
            ],
            options={
                'unique_together': {('place', 'weekday')},
            },
        ),
    ]