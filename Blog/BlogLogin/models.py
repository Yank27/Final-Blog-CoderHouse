import email
from email.mime import image
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.conf import settings

#Editar usuario / edit user
class UserUpdate(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Avatar for {self.user.username}"
