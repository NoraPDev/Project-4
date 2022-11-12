# Generated by Django 3.2 on 2022-11-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('photo', models.TextField()),
                ('short_description', models.TextField(default='')),
                ('preparation_guide', models.TextField()),
                ('difficulty', models.TextField()),
                ('ideal_for', models.TextField()),
                ('preparation_time', models.TextField()),
                ('ingredients', models.TextField()),
            ],
        ),
    ]
