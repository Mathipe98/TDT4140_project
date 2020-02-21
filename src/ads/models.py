from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Advertisement(models.Model):
    item = models.CharField(max_length=200)
    text = models.TextField(default='')
    pris = models.CharField(max_length=200, default='')
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', default=None)

    class Meta:
        managed = True
        app_label = 'ads'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_image_path(self):
        return 0

