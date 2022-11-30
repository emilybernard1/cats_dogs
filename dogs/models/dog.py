from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.breed}"

     