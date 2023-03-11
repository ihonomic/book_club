from django.urls import path
from .views import LandingPageView, CreateBookView


urlpatterns = [
    path('', LandingPageView.as_view(), name="Landing_Page"),
    path('create/', CreateBookView.as_view(), name="Create_Book"),
]
