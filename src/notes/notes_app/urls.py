from django.urls import path
from .import views

app_name = 'notes_app'
urlpatterns = [
    path('notes/',views.all_notes,name='all_notes'),
    path('one_note/<slug:slug>/',views.one_note,name='one_note'),
    path('add_note/',views.add_note,name='add_note'),
    path('<slug:slug>/edit_note/',views.edit_note,name='edit_note'),

]
