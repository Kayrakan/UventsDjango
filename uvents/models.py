from django.db import models

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.category_name


class Type(models.Model):
    type_name = models.CharField(max_length=80, blank=False, null=False)
    type_category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_name


class FanOption(models.Model):
    air_flow = models.IntegerField()
    pressure = models.IntegerField()
    fan_id = models.ForeignKey('Fan', on_delete = models.CASCADE, related_name='fan_options')

    def __str__(self):
        return f'Option: {self.id}'


class Fan(models.Model):
    fan_code = models.CharField(max_length=255, blank=False, null=False)
    max_airflow = models.IntegerField()
    min_airflow = models.IntegerField()
    max_pressure = models.IntegerField()
    min_pressure = models.IntegerField()
    image = models.TextField(blank=True)
    voltage = models.CharField(max_length=255)
    frequency = models.IntegerField()
    current = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    rpm = models.CharField(max_length=255)
    ip_code = models.CharField(max_length=255)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)
    fan_type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.fan_code
