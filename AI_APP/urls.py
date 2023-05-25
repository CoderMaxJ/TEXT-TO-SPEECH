from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
     path('registrationForm/',views.create,name="create"),
      path('codevalidation',views.login,name="login"),
      path('backendscript',views.saveInfo,name="backendscript"),
      path('userlist/',views.user,name='userlist'),
      path('appview',views.speak,name="appview"),
      path('admin_verification/',views.admincheck, name="check"),
        path('codevalidation/',views.gotologin, name="gotologin"),
       
      
    
      
    
]

