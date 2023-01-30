# Generated by Django 4.1.5 on 2023-01-25 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_reviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('Article_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=40)),
                ('Content', models.CharField(max_length=2000)),
                ('Reviewer_Id', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)])),
                ('Status', models.IntegerField()),
                ('Rating', models.IntegerField(default=None)),
            ],
        ),
    ]