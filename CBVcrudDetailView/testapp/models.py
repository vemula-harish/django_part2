from django.db import models
from django.urls import reverse
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})
