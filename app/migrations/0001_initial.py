# Generated by Django 4.2.3 on 2023-09-01 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('scname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('scprincipal', models.CharField(max_length=100)),
                ('sclocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=100)),
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('scname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
