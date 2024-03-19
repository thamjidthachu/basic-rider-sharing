from django.db import models

from apps.users.models import CustomUser


class Ride(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )
    rider = models.ForeignKey(CustomUser, related_name='rides_as_rider', on_delete=models.CASCADE)
    driver = models.ForeignKey(CustomUser, related_name='rides_as_driver', on_delete=models.CASCADE, null=True, blank=True)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
