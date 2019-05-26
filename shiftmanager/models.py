import datetime

from django.db import models

from .validators import csv_file_validator


class CustomDateField(models.DateField):
    def to_python(self, value):
        if value is None:
            return value
        return super().to_python(self.parse_date(value))
    
    def parse_date(self, value):
        return datetime.datetime.strptime(value, '%d/%m/%Y').date()


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shifts = models.ManyToManyField('Shift', related_name='employees', through='Roster')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shift(models.Model):
    date = CustomDateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_length = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} {self.start_time} {self.end_time} {self.break_length}"


class Roster(models.Model):
    WORKSHOP = 1
    FACTORY = 2
    SITE_CHOICES = [
        (WORKSHOP, 'Workshop'),
        (FACTORY, 'Factory'),
    ]

    employee = models.ForeignKey('Employee', related_name='roster', on_delete=models.CASCADE)
    slot = models.ForeignKey('Shift', related_name='roster', on_delete=models.CASCADE)
    site = models.IntegerField(choices=SITE_CHOICES, default=WORKSHOP)

    def __str__(self):
        return f"{self.employee} {self.slot} {self.get_site_display()}"


class Upload(models.Model):
    upload = models.FileField(validators=[csv_file_validator])
    uploaded_at = models.DateTimeField(auto_now_add=True)
