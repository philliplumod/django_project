from django.db import models
import uuid


class Member(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    data_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.member_id)
 