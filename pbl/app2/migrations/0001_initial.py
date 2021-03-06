# Generated by Django 3.0.6 on 2020-05-20 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivateDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('activate_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.ActivateDetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.UserDetail')),
            ],
        ),
        migrations.AddField(
            model_name='activatedetail',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.CourseDetail'),
        ),
    ]
