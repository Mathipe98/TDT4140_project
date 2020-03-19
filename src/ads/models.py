from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # Should optimally be used, not sure why user does not work
    return 'advertisements/user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    product_name = models.TextField(default="Product")
    product_description = models.TextField(default="There is no description available for this product.")
    price = models.IntegerField(default=0)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    sold_date = models.DateTimeField(blank=True, null=True)
    header_picture = models.ImageField(upload_to="ads/users/",  # Should create a folder for each user optimally
                                       default="ads/default.png")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        app_label = 'ads'

    def __str__(self):
        return "Seller name: " + " Price: " + str(self.price) \
            + "Dates: " + str(self.created_date) + " " + str(self.published_date) + \
               "Sold: " + str(self.sold)

    def get_seller_name(self):
        return self.seller

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def toggle_sold(self):
        self.sold = not self.sold
        return
