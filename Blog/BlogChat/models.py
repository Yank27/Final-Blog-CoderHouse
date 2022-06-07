from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

#-----------------------------------------------------------------------------------------------------------------------------------------------

class Chat(models.Model):
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
