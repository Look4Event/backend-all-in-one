# Generated by Django 4.0.5 on 2022-06-29 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beak.place')),
            ],
            options={
                'unique_together': {('place', 'weekday')},
            },
        ),
    ]
