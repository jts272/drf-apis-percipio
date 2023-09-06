from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    age = models.IntegerField()
    image = models.ImageField(
        upload_to="pictures", default="default_actors.jpeg"
    )
