# Generated by Django 5.0.2 on 2024-03-02 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maxlvl', models.IntegerField()),
                ('image', models.ImageField(upload_to='equipment/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.game')),
            ],
        ),
        migrations.CreateModel(
            name='Quests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.game')),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maxlvl', models.IntegerField()),
                ('image', models.ImageField(upload_to='spells/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.game')),
            ],
        ),
        migrations.CreateModel(
            name='Playthroughs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.game')),
            ],
            options={
                'unique_together': {('name', 'game', 'user')},
            },
        ),
    ]
