from django.urls import path
from main import views

urlpatterns=[
    path('homepage',views.homepage,name="homepage"),
    path('output',views.output,name="output"),
    path('doctor_output',views.doctor_output,name="doctor_output"),
    path('response',views.response,name="response"),
]