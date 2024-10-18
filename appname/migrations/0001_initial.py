# Generated by Django 5.1 on 2024-08-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicalid', models.IntegerField()),
                ('member1name', models.CharField(max_length=50)),
                ('member2name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SponserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponserid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SponserShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('sponserid', models.IntegerField()),
                ('amount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('location', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('no_year', models.IntegerField()),
            ],
        ),
    ]