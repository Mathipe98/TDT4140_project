from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# url imports
from sellyoshit.views import products, ad

# models imports
from ads.models import Category, Advertisement
from users.models import Users


class TestUrls(SimpleTestCase):
    """
    This class is testing the urls which makes the website browseable, these urls and views are contained
    in sellyoshit directory. Reverse returns the url if it exists within the project, and the url should have a func-
    method that corresponds to the correct view. Remark that the app name for these urls is 'shop', so in order
    to reverse the url you have to write shop:<url name>.
    """

    def test_products_url_resolves(self):
        url = reverse('shop:products')
        self.assertEquals(resolve(url).func, products)

    def test_ad_url_resolves(self):
        url = reverse('shop:details', kwargs={'pk': 1})  # details for ad number 1, specified by kwargs argument
        self.assertEquals(resolve(url).func, ad)


class TestViews(TestCase):
    """
    This class is testing the HTTP-response from the views. 200 OK if new HTML, or 302 if redirect. 400 is no response.
    It also assures that the templates are correct.
    """

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('shop:products')
        self.details_url = reverse('shop:details', kwargs={'pk': 1})

    def test_products_GET(self):
        response = self.client.get(reverse('shop:products'))
        self.assertEquals(response.status_code, 200)

        # all products are displayed by using product_listEXT.html which further extends base.html.
        self.assertTemplateUsed(response, 'sellyoshit/product_listEXT.html')

    def test_ad_GET(self):
        credentials = {
            'username': 'Georgyyy',
            'email': 'georgyboy@gmail.com',
            'password': 'a2bC90PqL345',
            'firstname': 'George',
            'lastname': 'Mc Twist'}
        seller = Users.objects.create_user(**credentials)
        category = Category.objects.create(name='TestCategory')
        product_car = Advertisement.objects.create(
            product_name="Car",
            product_description="Car",
            seller=seller,
            category=category
        )
        # response from the detail page for ad corresponding to product_car object
        response = self.client.get(reverse('shop:details', kwargs={'pk': product_car.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sellyoshit/product_details.html')
