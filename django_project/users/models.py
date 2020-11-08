from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameSurname = models.CharField(default="",max_length=40)
    companies = models.CharField(default="",max_length=120)
    experience = models.CharField(default="",max_length=120)
    aciklama = models.TextField(default="")
    oduller = models.TextField(default="")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    city = models.CharField(default='Istanbul',max_length=100)
    major = models.CharField(default='Computer Science',max_length=100)
    speciality = models.CharField(default="Python",max_length=100)
    Age = models.CharField(default="",max_length=5)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)