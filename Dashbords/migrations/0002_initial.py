# Generated by Django 5.1.3 on 2024-12-12 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dashbords', '0001_initial'),
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashbord',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Projects.project'),
        ),
    ]
