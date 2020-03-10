from django.db import models
# from authors.models import Author


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    author = models.ForeignKey(to="authors.Author", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"
