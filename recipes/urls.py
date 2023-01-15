from django.urls import path

from recipes.views import Contato, Home, Sobre

urlpatterns = [
    path('', Home),
    path('contato/', Contato),
    path('sobre/', Sobre),

]
