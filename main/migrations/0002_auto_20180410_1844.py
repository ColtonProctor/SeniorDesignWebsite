# Generated by Django 2.0.2 on 2018-04-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='caprate',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='condition',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='egi',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='exp',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='impsq',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='landsq',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='noi',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='occup',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='quality',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='units',
            field=models.CharField(default='none', max_length=10),
        ),
    ]
