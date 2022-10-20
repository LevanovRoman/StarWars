
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView
import requests
import json

# Create your views here.
class FilmsGallery(View):
    template_name = 'films/index.html'

    def get(self, request):
        resp =requests.get('https://swapi.dev/api/films/')
        obj = resp.json()
        return render(request, self.template_name, {"films": obj})

class FilmDetail(View):
    template_name = 'films/detail.html'

    def get(self, request):
        url = request.GET['url']
        resp = requests.get(url)
        return render(request, self.template_name, {"film": resp.json()})



