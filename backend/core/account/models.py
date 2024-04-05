from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone = models.CharField(null=True, max_length=255, blank=True)
    collections = models.ForeignKey(
        "UserCollection",
        on_delete=models.CASCADE,
    )

class UserCollections(models.Model):
    pass
