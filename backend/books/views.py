from django.shortcuts import render
from django.views import View

from .models import BookCategory, Book

# Two ways to write views. Class base views (CBV) and function base views (FBV)
# 4 types of requests. GET, POST, PUT, DELETE, (CRUD Operation)


class LandingPageView(View):
    template_name = "books/landing.html"

    def get(self, request):
        return render(request, self.template_name, {})


class CreateBookView(View):
    template_name = "books/create.html"
    # Fetch book categories
    categories = BookCategory.objects.all()
    context = {
        "categories": categories
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.method == 'POST':
            title = request.POST["title"]
            category_id = request.POST["category"]
            description = request.POST["description"]
            price = request.POST["price"]
            photo = request.POST["photo"]
            quantity = request.POST["quantity"]

            # print(title, category_id, description, price, photo, quantity)
            # get category instance
            # print(request.FILES, "<==== DEBUG")

            category_instance = BookCategory.objects.get(id=category_id)

            Book.objects.create(
                book_title=title,
                book_description=description,
                book_price=price,
                book_category=category_instance,
                book_image=photo,
                is_book_available=True,
                book_quantity=quantity
            )

        return render(request, self.template_name, self.context)
