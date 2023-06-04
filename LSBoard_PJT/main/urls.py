from django.urls import path
from . import views

app_name = "main"
 
urlpatterns = [
    path('', views.index, name='main_login'),
    path('CategoryRequest', views.CategoryResponse, name='CategoryMain'),
    path('programIntroRequest', views.ProgramIntroResponse, name='ProgramIntro'),
    path('programMathRequest', views.ProgramMathResponse, name='ProgramMath'),
]