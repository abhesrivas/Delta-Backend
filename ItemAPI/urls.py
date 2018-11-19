from django.urls import path, re_path
from ItemsAPI import views

urlpatterns = [
    #laptop/
    path('laptop/', views.LaptopList.as_view()),
    #laptop/1/
    re_path('laptop/(?P<pk>[0-9]+)/', views.LaptopDetail.as_view()),

    #rec2/
    path('rec2/', views.LocationRecommendation.as_view()),
]