from django.db import models
from account.models import UserAccount


class Museum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=500)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MuseumUser(models.Model):
    class Level(models.IntegerChoices):
        EMPLOYEE = 0
        MANAGER = 1
        MODERATOR = 2
        ADMINISTRATOR = 3
        OWNER = 4

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=30, default='Сотрудник')
    access_level = models.IntegerField(choices=Level, default=Level.EMPLOYEE)

    def __str__(self):
        return str(self.user)
