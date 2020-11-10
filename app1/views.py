from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

countries = {
    'USA'     : 'Washington DC', 
    'Canada'  : 'Ottawa',
    'England' : 'London',
    'France'  : 'Paris',
}

def home_page(request):
    return render(request, 'app1/home_page.html', {'countries': countries})
