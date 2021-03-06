# Generated by Django 3.0.3 on 2020-03-01 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('base', models.CharField(max_length=3)),
                ('target', models.CharField(max_length=3)),
                ('rate', models.DecimalField(decimal_places=10, max_digits=15)),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('base', 'target', 'rate', 'date')},
            },
        ),
    ]
