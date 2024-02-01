from django.urls import path
from . import views

app_name = 'playground'

urlpatterns = [
    path('home/', views.welcome),
    path('hello/<str:name>', views.hello, ),
    path('<int:number>/', views.number)

]