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
    path('profile_view',views.profile_view,name='profile_view'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('delete_profile',views.delete_profile,name='delete_profile'),
    path('contact',views.contact,name='contact'),
   
    
] 
