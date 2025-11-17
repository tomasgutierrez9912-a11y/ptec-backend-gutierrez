from django.db import models
from users.models import UserPlatform

class Device(models.Model):
    user_platform = models.ForeignKey(UserPlatform, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name