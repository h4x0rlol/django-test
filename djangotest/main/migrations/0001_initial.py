# Generated by Django 3.2.5 on 2021-07-09 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_time', models.DateTimeField(verbose_name='start_date_time')),
                ('data_volume', models.IntegerField(verbose_name='data_volume')),
                ('transmitted_data', models.IntegerField(verbose_name='transmitted_data')),
                ('transmitted_packets', models.IntegerField(verbose_name='transmitted_packets')),
                ('packages_without_errors', models.IntegerField(verbose_name='packages_without_errors')),
                ('packages_with_errors', models.IntegerField(verbose_name='packages_with_errors')),
                ('lost_packages', models.IntegerField(verbose_name='lost_packages')),
                ('average_speed', models.IntegerField(verbose_name='average_speed')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='rating')),
                ('isWork', models.BooleanField(verbose_name='isWork')),
                ('isCall', models.BooleanField(verbose_name='isCall')),
                ('id_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.list')),
            ],
        ),
    ]
