
from django.db import models
from housesell import settings
from property.models import Property


class Enquiry(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=200, blank=False)
    date_enquiry_made = models.DateTimeField(auto_now_add=True, editable=False)


def __str__(self):
    return self.person.username
