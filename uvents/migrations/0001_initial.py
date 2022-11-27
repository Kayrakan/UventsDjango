# Generated by Django 4.0.4 on 2022-05-16 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan_code', models.CharField(max_length=255)),
                ('max_airflow', models.IntegerField()),
                ('min_airflow', models.IntegerField()),
                ('max_pressure', models.IntegerField()),
                ('min_pressure', models.IntegerField()),
                ('image', models.TextField(blank=True)),
                ('voltage', models.CharField(max_length=255)),
                ('frequency', models.IntegerField()),
                ('current', models.CharField(max_length=255)),
                ('power', models.CharField(max_length=255)),
                ('rpm', models.CharField(max_length=255)),
                ('ip_code', models.CharField(max_length=255)),
                ('weigth', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=80)),
                ('type_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uvents.category')),
            ],
        ),
        migrations.CreateModel(
            name='FanOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_flow', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('fan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uvents.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='fan_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uvents.type'),
        ),
    ]