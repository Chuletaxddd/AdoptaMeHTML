from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def ong (request):
    
    return render(request, 'core/ong/inicio_ong.html')

