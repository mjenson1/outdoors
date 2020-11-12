from django.urls import path
from .views import indexPageView
from .views import rentalPageView
 
urlpatterns = [
    path("", indexPageView, name="index"),
    path("rental/", rentalPageView, name="rental")
]