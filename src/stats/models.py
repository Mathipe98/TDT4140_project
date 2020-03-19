from django.db import models
from ads.models import Advertisement
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

User = settings.AUTH_USER_MODEL

"""class ObjectViewed(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True, null=True)  #User instance
    ip_address = models.CharField(max_length=220, blank=True, null=True) #IP field
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING) #Advertisement etc (any model)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') #Advertisement instance
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed %s" % (self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp'] # most recent saved show up first
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'"""
    



