# Generated by Django 4.1.2 on 2023-01-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_gamematrix_p_11_remove_gamematrix_p_12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamematrix',
            name='matrix_map',
            field=models.CharField(default='[11,12,13,21,22,23,31,32,33]', max_length=50),
        ),
    ]
