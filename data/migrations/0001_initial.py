# Generated by Django 2.2.3 on 2020-01-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], default='monday', max_length=20)),
                ('date', models.DateField()),
                ('high', models.IntegerField(default=1)),
                ('low', models.IntegerField(default=1)),
                ('average', models.FloatField()),
                ('wind', models.IntegerField(default=1)),
            ],
        ),
    ]