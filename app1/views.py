from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def home_page(request):
    dct = {'one': 'ek', 'two': 'do', 'teen': 'teen'}
    return render(request, 'app1/home_page.html', {'dct': dct})
