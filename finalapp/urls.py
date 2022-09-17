from django.urls import path, include

from finalapp import views

app_name = 'finalapp'

urlpatterns = [

    path('', views.home, name='home'),
    path('registerform/', views.registerform, name='registerform'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('button/', views.button, name='button'),
    path('registerr/', views.registerr, name='registerr'),
    path('districtdetail', views.districtdetail, name='districtdetail'),
    path('<slug:d_slug>/', views.districtdetail, name='d_by_details'),
    path('load_branches/', views.load_branches, name='load_branches'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX

]
