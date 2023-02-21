from django.urls import path
import profil.views as views

app_name = 'profil'

urlpatterns = [
    path('', views.index, name="home"),
    path('templates/landing/login/', views.login_view, name="login"),
    path('templates/landing/signup/', views.signup_view, name="signup"),
    path('templates/landing/logout/', views.logout_view, name="logout")
]