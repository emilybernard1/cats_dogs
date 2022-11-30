from django.db import models

# Create your models here.
class Cat(models.Model):
    first_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.breed}"

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'breed': self.breed,
        }