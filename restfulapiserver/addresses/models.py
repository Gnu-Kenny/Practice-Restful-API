from django.db import models
# from django.contrib.auth.models import User as Default_User
# Create your models here.


class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


# class User(Default_User):
#     isAdmin = models.BooleanField(default=False)
