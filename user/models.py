from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum


class Role(Enum):
    FARMER = "farmer"
    CUSTOMER = "customer"
    ADMIN = "admin"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

ROLE_CHOICES = (
    ("FARMER", "Farmer"),
    ("CUSTOMER", "Customer"),
    ("ADMIN", "Admin"),
)

class User(AbstractUser):
    telegram_id = models.IntegerField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="CUSTOMER")




