
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import requests
import json

# Create your views here.
class FilmsGallery(View):
    template_name = 'films/index.html'

    def get(self, request):
        resp =requests.get('https://swapi.dev/api/films/1/')
        obj = resp.json()
        return render(request, self.template_name, {"film": obj})


