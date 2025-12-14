from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Base user for authentication
    pass

class Customer(models.Model):
    """
    Alohid user modeli, faqat xaridorlar uchun.
    Oddiy User modeli bilan OneToOne orqali bog'lanadi, lekin ma'lumotlar alohida saqlanadi.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, help_text="Yetkazib berish manzili")
    
    # Qo'shimcha ma'lumotlar
    date_of_birth = models.DateField(null=True, blank=True)
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return f"Customer: {self.user.username}"
