# Generated by Django 5.0.2 on 2024-03-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(upload_to='tracker/'),
        ),
        migrations.AlterField(
            model_name='spells',
            name='image',
            field=models.ImageField(upload_to='tracker/'),
        ),
    ]
