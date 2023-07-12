from django.db import models

# Create your models here.

from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    job_position = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name