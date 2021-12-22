from django.shortcuts import render
from django.http import HttpResponse
from django import views


class BaseViews(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})
