from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
