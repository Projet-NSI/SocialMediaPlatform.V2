from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import FileResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

#affiche la page d'accueil du site 
class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')


