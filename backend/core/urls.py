from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret-center/', admin.site.urls),
    path("", include("books.urls")),
    # path("users/", include("users.urls")),
]
