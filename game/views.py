from django.shortcuts import render
from django.http import HttpResponse



def show_phones(request):
    return render(request, 'base.html')
