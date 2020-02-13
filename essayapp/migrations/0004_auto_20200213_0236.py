# Generated by Django 3.0.2 on 2020-02-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essayapp', '0003_auto_20200212_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('subcategory', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Essay1',
        ),
    ]