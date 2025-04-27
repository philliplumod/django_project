from django.db import models
import uuid


class Member(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return str(self.member_id)
