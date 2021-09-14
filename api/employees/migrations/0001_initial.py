# Generated by Django 3.2.7 on 2021-09-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=3)),
                ('email_id', models.EmailField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
    ]