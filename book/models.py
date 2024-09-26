from django.db import models
from django.db.models import CheckConstraint, Q

class BookCategory(models.Model):
    name = models.TextField(default = "Not categorized")

# Create your models here.
class Book(models.Model):
    RATINGS = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five')
    )

    STATUS = (
        ('In stock', 'In stock'),
        ('Low in stock', 'Low in stock'),
        ('Out of stock', 'Out of stock'),
    )

    title = models.TextField(default = "Unknown")
    category = models.ForeignKey(BookCategory, on_delete = models.CASCADE, related_name="category")
    rating = models.PositiveBigIntegerField(choices = RATINGS, blank = True, null = True)
    price = models.DecimalField(max_digits=20,decimal_places=2, default=0)
    stock = models.CharField(max_length=30, choices=STATUS, default='Out of stock')
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(
                condition = Q(quantity__gte=0),
                name = "check_stock_non_negative"
            )
        ]


