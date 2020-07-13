from django.shortcuts import render
from main.models import Patient
from main.forms import PatientForm 
from django.shortcuts import redirect
from datetime import date, timedelta


# Create your views here.
def homepage(request):
    form = PatientForm()
    if request.method == 'POST':
        form =PatientForm(request.POST,request.FILES)
        if form.is_valid():
            instance = Patient(reportFirst=request.FILES['reportFirst'],reportSecond=request.FILES['reportSecond'])
            instance.save()
            form.save()
            print('valid')
            return redirect('/homepage')
        else:
            print('invalid')

    context={
        "form":form,
    }

    return render(request,'main/homepage.html',context)


def test(request):
    context={}
    return render(request,'main/test.html',context)


def output(request):
    appoint=Patient.objects.all().last()
    age = (date.today() - appoint.dob) // timedelta(days=365.2425)
    weight_gain=(appoint.weight9/(appoint.weight-appoint.weight9))*100
    weight_gained=round(weight_gain,2)
    waisthip=appoint.waist/appoint.hip
    waist_hip=round(waisthip,2)
    height=(appoint.height_feet*30.48+appoint.height_inches*2.54)/100
    BMI=appoint.weight/(height*height)
    bmi=round(BMI,2)

    pcos_sum=0

    if appoint.missedPeriod == "true":
      pcos_sum+=5

    if appoint.extraHair == "true":
        pcos_sum+=4

    if appoint.acneLoss == "true":
        pcos_sum+=4

    if appoint.hairLoss == "true":
        pcos_sum+=3

    if appoint.moodSwings == "true":
        pcos_sum+=2

    pcos_ratio=pcos_sum/18

    thyroid_sum=0

    if appoint.moodSwings == "true":
        thyroid_sum+=5

    if appoint.constipation == "true":
        thyroid_sum+=4

    if appoint.missedPeriod == "true":
        thyroid_sum+=4

    if appoint.skinPigmentation == "true":
        thyroid_sum+=3

    if appoint.slowHeartbeat == "true":
        thyroid_sum+=2

    if appoint.headache == "true":
        thyroid_sum+=2

    thyroid_ratio=thyroid_sum/20

    prolac_sum=0

    if appoint.dischargeNipple == "true":
        prolac_sum+=5

    if appoint.missedPeriod == "true":
        prolac_sum+=4

    if appoint.headache == "true":
        prolac_sum+=3

    if appoint.moodSwings == "true":
        prolac_sum+=3

    prolac_ratio=prolac_sum/17



    

    

    

    print(appoint)
    context={
        "appoint":appoint,
        "age":age,
        "waist_hip":waist_hip,
        "weight_gained":weight_gained,
        "bmi":bmi,
        "pcos_ratio":pcos_ratio,
        "thyroid_ratio":thyroid_ratio,
        "prolac_ratio":prolac_ratio
    }
    return render(request,'main/output.html',context)


