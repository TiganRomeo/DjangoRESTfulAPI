from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username