from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('querypage', views.querypage, name='querypage'),
    path('generate', views.generate, name='generate'),
    path('explain', views.explain_page, name='explain')

]