from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Orders
from django.conf import settings


BrandUser = settings.BRAND_USER_MODEL


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['id','tracking_number', 'status', 'sender', 'receiver', 'origin', 'destination','estimated_delivery', 'details', 'created_at']







