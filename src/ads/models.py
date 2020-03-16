from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # Should optimally be used, not sure why user does not work
    return 'advertisements/user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])



class Advertisement(models.Model):
    product_name = models.TextField(default="Product")
    product_description = models.TextField(default="There is no description available for this product.")
    price = models.IntegerField(default=0)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    header_picture = models.ImageField(upload_to="ads/users/",  # Should create a folder for each user optimally
                                       default="ads/default.png")
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=False)

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

    def get_cat_list(self):
        k = self.category

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]
