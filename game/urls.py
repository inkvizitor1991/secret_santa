from django.urls import path
from .views import BaseViews,RegistrationView,LoginView



urlpatterns = [
    path('',BaseViews.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),

]