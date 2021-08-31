from django.db import models
import uuid

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=False,null=False)
    age = models.IntegerField(default=0)

    class Meta:
        db_table = "tbl_dog"
        ordering = ['id']

    def __str__(self):
        return self.name
    