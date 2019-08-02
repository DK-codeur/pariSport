from django.shortcuts import render, get_object_or_404
from myapp.models import *


def home(request):
    context = {
        'battles': Battle.objects.all()
    }
    return render(request, 'pages/home.html', context)


def pari(request, id):

    ch = get_object_or_404(Battle, pk=id)
    return render(request, 'pages/pari.html', {'ch': ch})
