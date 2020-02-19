# Create your models here.
from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # Should optimally be used, not sure why user does not work
    return 'advertisements/user_{0}/{1}'.format(instance.user.id, filename)


class Advertisement(models.Model):
    product_name = models.TextField(default="Product")
    price = models.IntegerField(default=0)
    seller_name = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    header_picture = models.ImageField(upload_to="ads/users/",
                                       default="ads/default.png")

    def __str__(self):
        return "Seller name: " + self.seller_name + " Price: " + str(self.price) \
            + "Dates: " + str(self.created_date) + " " + str(self.published_date) + \
               "Sold: " + str(self.sold)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        return

    def sell(self):
        self.sold = True
        return
