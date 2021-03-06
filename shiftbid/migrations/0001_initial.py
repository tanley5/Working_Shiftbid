# Generated by Django 4.0.4 on 2022-05-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shfitbid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftbid_name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('shift_status', models.CharField(choices=[('c', 'created'), ('s', 'started'), ('e', 'stopped')], default='c', max_length=1)),
            ],
        ),
    ]
