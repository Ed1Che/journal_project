from django.db import models
from django.contrib.auth.models import User  # Django's built-in User model

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)  # Added for tracking modifications

    def __str__(self):
        return self.title