from django.urls import path
import profil.views as views
from .views import index

urlpatterns = [
    path('', index.as_view(), name="home"),
]