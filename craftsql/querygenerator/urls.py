from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('querypage', views.querypage, name='querypage'),
    path('generate', views.generate, name='generate'),
    path('explain', views.explain_page, name='explain'),
    path('explainsql', views.explain_sql, name='explainsql'),
    path('fix', views.fixpage, name='fixpage'),
    path('fixquery', views.fix_query, name='fixquery'),
    path('suggest', views.suggest, name='suggest'),
    path('suggest_optimization', views.suggest_optimization,
         name='suggest_optimization')

]
