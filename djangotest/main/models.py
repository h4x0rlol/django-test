from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class List(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("name", max_length=50)

    def __str__(self):
        return self.name


class Session(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField("start_date_time")
    data_volume = models.IntegerField("data_volume")
    transmitted_data = models.IntegerField("transmitted_data")
    transmitted_packets = models.IntegerField("transmitted_packets")
    packages_without_errors = models.IntegerField("packages_without_errors")
    packages_with_errors = models.IntegerField("packages_with_errors")
    lost_packages = models.IntegerField("lost_packages")
    average_speed = models.IntegerField("average_speed")


class Frequency(models.Model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE)
    rating = models.IntegerField("rating")
    isWork = models.BooleanField("isWork")
    isCall = models.BooleanField("isCall")


class Band(models.Model):
    bandwidth: models.IntegerField("bandwidth")
