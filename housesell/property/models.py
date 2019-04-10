from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

PROPERTY_CITY_CHOICES = (
    ('Kanpur', 'Kanpur'),
    ('New Delhi', 'New Delhi'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Chandigarh', 'Chandigarh'),
)
PROPERTY_STATE_CHOICES = (
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Delhi', 'Delhi'),
    ('Karnataka', 'Karnataka'),
    ('Punjab', 'Punjab'),
)


class Property(models.Model):
    property_poster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='property', on_delete=models.CASCADE)
    property_title = models.CharField(max_length=20)
    property_address = models.CharField(max_length=20)
    property_city = models.CharField(max_length=20, choices=PROPERTY_CITY_CHOICES)
    property_states = models.CharField(max_length=20, choices=PROPERTY_STATE_CHOICES)
    property_pin = models.IntegerField(blank=False)
    property_price = models.IntegerField(blank=False)
    property_bedroom = models.IntegerField(blank=False)
    property_bathroom = models.IntegerField(blank=False)
    property_sq_feet = models.IntegerField(blank=False)
    property_lot_size = models.IntegerField(default=0)
    property_garage = models.IntegerField(default=0)
    property_is_published = models.BooleanField(default=True)
    property_listing_date = models.DateField(auto_now_add=True, editable=False)
    property_description = models.TextField(max_length=200, blank=True)
    photo_main = models.ImageField(upload_to='property_images/', default='property_images/default/home.jpg')
    photo1 = models.ImageField(upload_to='property_images/', blank=True)
    photo2 = models.ImageField(upload_to='property_images/', blank=True)
    photo3 = models.ImageField(upload_to='property_images/', blank=True)
    photo4 = models.ImageField(upload_to='property_images/', blank=True)
    photo5 = models.ImageField(upload_to='property_images/', blank=True)
    photo6 = models.ImageField(upload_to='property_images/', blank=True)

    def __str__(self):
        return self.property_title
