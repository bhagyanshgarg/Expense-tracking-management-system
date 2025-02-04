from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_premium = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Fixes conflict
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Fixes conflict
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
