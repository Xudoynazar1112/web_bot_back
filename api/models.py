from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_images/')
    price = models.IntegerField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
