from django.urls import path
from . import views
from .views import  index
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', index, name='dashboard'),
    path('obter_resposta_ia/', views.obter_resposta_ia_view),
    path('logout/', views.logout_view, name='logout'),
   

    
   
    
    
    
    
]

