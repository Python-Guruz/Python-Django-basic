# Generated by Django 3.2.5 on 2021-08-31 09:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0002_auto_20210831_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]