from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()
    shared_with = models.ManyToManyField(User, related_name="shared_expenses", blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Settled', 'Settled')])

    def __str__(self):
        return self.title
