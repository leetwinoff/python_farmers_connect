import uuid

from django.db import models

from user.models import User

PRODUCT_TYPE_CHOICES = (
        ("FRU", "Fruit"),
        ("VEG", "Vegetable"),
        ("DIA", "Diary"),
    )

UNIT_CHOICES = (
    ("KG", "Kilogram"),
    ("ML", "Milligram"),
    ("PKG", "Package"),
    ("BX", "Box"),
)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farmer = models.ForeignKey("Farmer", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consumer = models.ForeignKey("Consumer", on_delete=models.CASCADE)
    farmer = models.ForeignKey("Farmer", on_delete=models.CASCADE)
    comment = models.TextField(max_length=1200)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Farmer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='farmers')
    rating = models.PositiveIntegerField(default=0)
    reviews = models.ManyToManyField(Review, related_name='farmers', blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.company_name}"


class Consumer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    reviews = models.ManyToManyField(Review, related_name='customers', blank=True)
    saved_farmers = models.ManyToManyField(Farmer, related_name='saved_by', blank=True)
    saved_products = models.ManyToManyField(Product, related_name='saved_by', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()



