from django.db import models

# Create your models here.


class BookCategory(models.Model):
    category_name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)


class Book(models.Model):
    book_title = models.CharField(max_length=256)
    book_description = models.TextField()
    book_price = models.FloatField()
    book_category = models.ForeignKey(
        BookCategory, on_delete=models.CASCADE, related_name="book_category_instance")
    is_book_available = models.BooleanField(default=True)
    book_quantity = models.IntegerField(default=0)
    book_image = models.ImageField(
        upload_to="book", default="https://banner2.cleanpng.com/20180329/vke/kisspng-python-high-level-programming-language-language-5abd4cc0d3dc94.7432282215223553928678.jpg")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.book_title)
