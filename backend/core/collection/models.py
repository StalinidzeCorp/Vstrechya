from django.db import models

from account.models import UserAccount
from museum.models import Museum


class Collection(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserCollection(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user_id', 'collection_id']


class MuseumCollection(models.Model):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Коллекция музея'
        verbose_name_plural = 'Коллекции музеев'

    def __str__(self):
        return str(self.museum)


class CollectionItem(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
