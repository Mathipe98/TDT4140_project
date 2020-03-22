"""
    Django database models for Advertisements and Categories

    classes
        Category:
            The category for an Advertisement
        Advertisement:
            A product to be sold on the site by someone

"""
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
        The category for an Advertisement

        Attributes
            name : CharField
                The name of the category

        Functions
            __str__ : str
                toString returning the name of the category
    """
    name = models.CharField(max_length=40)

    def __str__(self):
        """Returns the name of the category"""
        return self.name


class Advertisement(models.Model):
    """
        A product to be sold on the site by someone

        Attributes
            product_name : TextField
                The name of the product
            product_description: TextField
                Description of the product
            price : PositiveIntegerField
                Price of the product
            seller: ForeignKey
                The seller of the product
            created_date: DateTimeField
                The date and time the advertisement was created
            published_date: DateTimeField
                The date and time the advertisement was last published
            sold : BooleanField
                Whether or not the product has been sold yet
            sold_date : DateTimeField
                The date and time the advertisement was sold
            header_picture: ImageField
                An image of the product
            category: ForeignKey
                Which category the product falls under

        Functions
            __str__ : String
                toString for the Advertisement model
            publish: None
                Sets the published_date to current time
            toggle_sold: None
                Inverts the sold value of the product

    """
    product_name = models.TextField()
    product_description = models.TextField()
    price = models.PositiveIntegerField(default=0)  # default=0 sets the price to 0 unless otherwise specified
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # References the seller model
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    sold_date = models.DateTimeField(blank=True, null=True)
    header_picture = models.ImageField(upload_to="ads/users/",  # The folder to which the image will be uploaded
                                       default="ads/default.png")  # If no image is uploaded, this will be displayed
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # References the category model

    class Meta:
        """ Meta class for Advertisement"""
        managed = True  # Whether or not the model is added to the database
        app_label = 'ads'  # TODO: Explain this line

    def __str__(self):
        """Returns toString for Advertisement model"""
        return "Seller name: " + " Price: " + str(self.price) \
               + "Dates: " + str(self.created_date) + " " + str(self.published_date) + \
               "Sold: " + str(self.sold)

    def publish(self):
        """Updates the published_date attribute to timezone.now(). Returns None"""
        self.published_date = timezone.now()
        self.save()

    def toggle_sold(self):
        """Inverts the sold property. Returns None"""
        self.sold = not self.sold
