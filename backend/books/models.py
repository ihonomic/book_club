from django.db import models

# Create your models here.


class BookCategory(models.Model):
    category_name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.category_name)


class Book(models.Model):
    book_title = models.CharField(max_length=256)
    book_description = models.TextField()
    book_price = models.FloatField()
    book_category = models.ForeignKey(
        BookCategory, on_delete=models.CASCADE, related_name="book_category_instance")
    is_book_available = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.book_title)
