from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


app_name = 'accounts'
urlpatterns = [ 
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/<slug:slug>/',views.profile,name='profile'),
    path('edit_profile/<slug:slug>/',views.edit_profile,name='edit_profile'),
    path('change_password/<slug:slug>/',views.change_password,name='change_password'),
]
