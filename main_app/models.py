from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Treasures(models.Model):
    """
    Model class for the Treasures
    The user column will be marked as a Foreign key, which will allow one user to have many treasures.
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # location in the media directory to add images to and a default image in case it is None
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')

    def __str__(self):
        return self.name
