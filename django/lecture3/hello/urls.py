from django.urls import path
from . import views
urlpatterns =[
    path("", views.index, name = "index"),
    path("minhong", views.minhong, name = "minhong"),
    path("<str:name>", views.greet, name = "greet"),
]