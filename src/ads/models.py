from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # Should optimally be used, not sure why user does not work
    return 'advertisements/user_{0}/{1}'.format(instance.user.id, filename)

class Advertisement(models.Model):
    product_name = models.TextField(default="Product")
    product_description = models.TextField(default="There is no description available for this product.")
    price = models.IntegerField(default=0)
    seller_name = models.TextField()  # Should be replaced by a user
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    # Should add a description field to the advertisement
    header_picture = models.ImageField(upload_to="ads/users/",  # Should create a folder for each user optimally
                                       default="ads/default.png")
    class Meta:
        managed = True
        app_label = 'ads'

    def __str__(self):
        return "Seller name: " + self.seller_name + " Price: " + str(self.price) \
            + "Dates: " + str(self.created_date) + " " + str(self.published_date) + \
               "Sold: " + str(self.sold)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def toggle_sold(self):
        self.sold = not self.sold
        return

    def update_name(self, new_name):
        assert isinstance(new_name, str)
        if new_name == "":
            return "You cannot set the name to empty"
        elif len(new_name) > 60:
            return "New name cannot be longer than 60 characters"
        else:
            self.product_name = new_name
            return "Successfully updated"

    def update_description(self, new_description):
        assert isinstance(new_description, str)
        if new_description == "":
            self.product_description = "There is no description available for this product."
            # Not sure if this works as intended
            return
        elif len(new_description) > 400:
            return "Description can't be longer than 400 chars"
        else:
            self.product_description = new_description
            return "Successfully updated"

    def update_price(self, price):
        try:
            price = int(price)
        except ValueError:
            return "Price must be an integer"
        self.price = price
        return

