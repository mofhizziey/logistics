from django.db import models
from django.conf import settings
import uuid
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

from django.contrib.auth import get_user_model
User = get_user_model()
RANDOM_ORDER_ID = get_random_string(length=12)


# FIXED: Order model with proper null handling
class Orders(models.Model):
    # FIXED: Allow null user for guest checkout or handle appropriately
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', null=True, blank=True)
    tracking_number = models.CharField(max_length=250, default='', null=True)

    status = models.CharField(
        max_length=250,
    )
    sender = models.CharField(
        max_length=255,
      
    )
    receiver = models.CharField(
        max_length=250,
     
    )
    origin = models.CharField(
        max_length=255,
       
    )
    destination = models.CharField(
        max_length=255,
  
    )
    estimated_delivery = models.DateField(
        null=True,
        blank=True,
       
    )
    details = models.TextField(
        blank=True,
        null=True,
      
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
       
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    
    )

    def __str__(self):
        return f'{self.tracking_number}'