from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    username = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
