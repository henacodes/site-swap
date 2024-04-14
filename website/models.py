from django.db import models

# Create your models here.


class Website(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    description = models.TextField(default="")

    def __str__(self) -> str:
        return self.name