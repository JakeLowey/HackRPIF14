from django.db import models
from django.contrib import admin

# Create your models here.


# class User(models.Model):
#     user_name = models.TextField()
#     password = models.TextField()
#     first_name = models.TextField()
#     last_name = models.TextField()
#
#
# class UserInfo(models.Model):
#     UserID = models.ForeignKey(User)
#     school = models.TextField()
#     steam_name = models.TextField()
#     num_attended = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)