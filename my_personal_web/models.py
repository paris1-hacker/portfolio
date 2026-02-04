from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.TextField()
    email = models.EmailField()
    product = models.TextField()
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.name
