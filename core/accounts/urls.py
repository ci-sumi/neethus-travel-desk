from django.contrib import admin
from django.urls import path
from .import views
from .views import CustomLogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',CustomLogoutView.as_view(),name='logout'),
    path('contact',views.contact,name='contact'),
    path('destinations_list/',views.destination_list,name='destination_list'),
    path('destinations/new',views.destination_create,name='destination_create'),
    path('destination_detail/<int:pk>/',views.destination_detail,name='destination_detail'),
] 
