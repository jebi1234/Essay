# Generated by Django 3.0.2 on 2020-02-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essayapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay1',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('college', models.CharField(max_length=150)),
                ('roll_no', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('essay', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Essay',
        ),
    ]
