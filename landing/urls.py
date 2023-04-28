from django.urls import path
from .views import index

#chemins des urls, qui prends pour vue 'index'
urlpatterns = [
    path('', index.as_view(), name="index"),
]