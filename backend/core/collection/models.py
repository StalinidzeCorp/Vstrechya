from django.db import models

from account.models import UserAccount


class Collection(models.Model):
    name = models.CharField(max_length=255)

class UserCollection(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['user_id', 'collection_id']


class CollectionItem(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

