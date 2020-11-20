from django.urls import path
from .import views

app_name = 'home'
urlpatterns = [
    path('all-notes/',views.allnotes,name='all-notes'),
    

]
