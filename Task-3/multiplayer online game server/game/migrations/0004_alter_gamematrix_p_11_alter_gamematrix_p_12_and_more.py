# Generated by Django 4.1.2 on 2023-01-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_gamematrix_game_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamematrix',
            name='p_11',
            field=models.CharField(default='11', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_12',
            field=models.CharField(default='12', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_13',
            field=models.CharField(default='13', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_21',
            field=models.CharField(default='21', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_22',
            field=models.CharField(default='22', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_23',
            field=models.CharField(default='23', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_31',
            field=models.CharField(default='31', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_32',
            field=models.CharField(default='32', max_length=1),
        ),
        migrations.AlterField(
            model_name='gamematrix',
            name='p_33',
            field=models.CharField(default='33', max_length=1),
        ),
    ]
