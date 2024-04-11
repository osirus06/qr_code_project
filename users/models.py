from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    rank = models.CharField(max_length=50)
    SECURITY_CLEARANCE_CHOICES = [
        ('LEVEL_1', 'Level 1'),
        ('LEVEL_2', 'Level 2'),
        ('LEVEL_3', 'Level 3'),
    ]
    security_clearance = models.CharField(max_length=20, choices=SECURITY_CLEARANCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.TextField()  # Stores the base64 encoded QR code image
