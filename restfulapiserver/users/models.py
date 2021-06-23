from django.db import models
from django.contrib.auth.models import User as Default_User
# Create your models here.


class User(Default_User):
    isAdmin = models.BooleanField(default=False)
