# Generated by Django 3.0.2 on 2020-02-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essayapp', '0005_auto_20200213_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('lang', models.CharField(max_length=150)),
                ('essay', models.CharField(max_length=20000)),
            ],
        ),
    ]