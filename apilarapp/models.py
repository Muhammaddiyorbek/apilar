from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    content=models.TextField()
    author=models.CharField(max_length=250)
    isbn=models.CharField(max_length=13)
    price=models.DecimalField(max_digits=250,decimal_places=2)

    def __str__(self):
        return self.title