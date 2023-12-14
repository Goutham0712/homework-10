#Open the file contactsapi/models.py and edit:

from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

#Open the file contactsapi/admin.py and edit:
