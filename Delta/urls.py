from django.contrib import admin
from django.urls import path, re_path
from ItemAPI import views
from rest_framework.urlpatterns import format_suffix_patterns
#from UserAPI import views as user_views

urlpatterns = [
    
    #admin/
    path('admin/', admin.site.urls),

    #laptop/
    path('laptop/', views.LaptopList.as_view()),
    #laptop/1/
    re_path('laptop/(?P<pk>[0-9]+)/', views.LaptopDetail.as_view()),
    
    #laptop/?page=1
    #List the first page

]