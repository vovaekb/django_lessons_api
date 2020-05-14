from django.db import models

class Teacher(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    imageUrl = models.URLField(max_length=200)

class Lessons(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    startTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)
    weekDay = models.IntegerField()
    appointment_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    availability = models.IntegerField()
