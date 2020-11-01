from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    img = models.FileField()
    