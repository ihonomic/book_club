from django.shortcuts import render
from django.views import View

# Two ways to write views. Class base views (CBV) and function base views (FBV)
# 4 types of requests. GET, POST, PUT, DELETE, (CRUD Operation)


class LandingPageView(View):
    template_name = "books/landing.html"

    def get(self, request):
        return render(request, self.template_name, {})
