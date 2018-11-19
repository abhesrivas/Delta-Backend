from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from UserAPI import views as user_views
from ItemAPI import views

urlpatterns = [

    #admin/
    path('admin/', admin.site.urls),

    #users/
    path('users/', user_views.UserList.as_view()),

    #users/1/
    re_path('users/(?P<pk>[0-9]+)/', user_views.UserDetail.as_view()),

    #profiles/
    path('profiles/', user_views.ProfileList.as_view()),

    #profiles/1/
    re_path('profiles/(?P<pk>[0-9]+)/', user_views.ProfileDetail.as_view())

    #laptop/
    path('laptop/', views.LaptopList.as_view()),

    #laptop/1/
    re_path('laptop/(?P<pk>[0-9]+)/', views.LaptopDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
