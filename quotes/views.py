from django.shortcuts import render
from .models import Quote

# Create your views here.

def home(request):
    quote = Quote.objects.order_by('?').first()
    return render(request, 'home.html', {'quote': quote})