from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'Main/index.html')