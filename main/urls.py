from django.urls import path
from main import views

urlpatterns=[
    path('www.proactiveforher.com/tools/weight-gain-patient-information/input',views.homepage,name="homepage"),
    path('www.proactiveforher.com/tools/weight-gain-patient-information/output',views.output,name="output"),
    path('www.proactiveforher.com/tools/access-weight-gain-patient-information',views.doctor_output,name="doctor_output"),
    path('response',views.response,name="response"),
]