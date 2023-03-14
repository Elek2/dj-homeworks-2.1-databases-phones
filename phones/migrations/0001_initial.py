# Generated by Django 4.1.7 on 2023-03-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('release_date', models.DateField(default='2023-03-05')),
                ('lte_exists', models.BooleanField(default=0)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]