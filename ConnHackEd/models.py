from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()

class UserInfo(models.Model):
    UserID = models.ForeignKey(User)
    school = models.TextField()
    steam_name = models.TextField()
    num_attended = models.IntegerField()

