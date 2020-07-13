from django.urls import path
from main import views

urlpatterns=[
    path('homepage',views.homepage,name="homepage"),
    path('test',views.test,name="test"),
    path('output',views.output,name="output")
]