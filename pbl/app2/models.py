from django.db import models

# Create your models here.
from django.db.models import CASCADE


class CourseDetail(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class ActivateDetail(models.Model):
    id = models.AutoField(unique=True,primary_key = True)
    activate_name = models.CharField(max_length=100)
    course = models.ForeignKey('CourseDetail', on_delete=CASCADE)

    def __str__(self):
        return self.activate_name


class UserDetail(models.Model):
    id = models.AutoField(unique=True,primary_key = True)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class UserActivity(models.Model):
    id = models.AutoField(unique=True,primary_key = True)
    name = models.CharField(max_length=100)
    activity = models.ForeignKey('ActivateDetail',on_delete=CASCADE)
    user = models.ForeignKey(UserDetail,on_delete=CASCADE)

    def __str__(self):
        return self.name