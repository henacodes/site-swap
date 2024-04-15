from django.db import models
import random
import string

def generate_random_string(length):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length ))



# Create your models here.
def get_image_file_path(self, filename):
    print("file name")
    print(filename)
    return f'site_screenshots/{self.name}_{generate_random_string(6)}.jpg'


class Website(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    description = models.TextField(default="")
    screenshot = models.ImageField(max_length=255, upload_to=get_image_file_path, blank=True )

    REQUIRED_FIELDS = ["name", "link"]

    def __str__(self) -> str:
        return self.name