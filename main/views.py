from django.shortcuts import render
from main.models import Patient,DoctorOutput
from main.forms import PatientForm,DoctorOutputForm,FooterForm
from django.shortcuts import redirect
from datetime import date, timedelta


# Create your views here.
def homepage(request):
    form = PatientForm()
    if request.method == 'POST':
        form =PatientForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = Patient(reportFirst=request.FILES['reportFirst'],reportSecond=request.FILES['reportSecond'])
            #print(instance)
            #instance.save()
            form.save()
            print('valid')
            return redirect('/output')
        else:
            print('invalid')

    today_month=date.today().month
    today_year=date.today().year

    form1 = FooterForm()

    

    context={
        "form":form,
        "today_month":today_month,
        "today_year":today_year,
        "form1":form1
        
    }

    return render(request,'main/homepage.html',context)




def output(request):
    appoint=Patient.objects.all().last()
    if appoint.dob == None:
        age =""
    else:
        age = (date.today() - appoint.dob) // timedelta(days=365.2425)



    
    if appoint.weight == None or appoint.weight9 == None:
        weight_gained="n"
    else:
        weight_gain=(appoint.weight9/(appoint.weight-appoint.weight9))*100
        weight_gained=round(weight_gain,2)

    


    if appoint.waist == None or appoint.hip == None:
        waist_hip=0
    else:
        waisthip=appoint.waist/appoint.hip
        waist_hip=round(waisthip,2)



    if appoint.height_feet == None :
        height=0
    else:
        if appoint.height_inches == None:
            appoint.height_inches =0 
        height=(appoint.height_feet*30.48+appoint.height_inches*2.54)/100

    


    if appoint.weight == None or height == 0 :
        bmi=0
    else:
        BMI=appoint.weight/(height*height)
        bmi=round(BMI,2)




    if height == 0:
        ideal_weight=""
    else:
        ideal_weight=24.9*height*height

   

    
    weightbmi=0

    if bmi == 0:
        Weightbmi="n"

    else:

        if bmi >= 25:
            weightbmi = appoint.weight - ideal_weight

        elif bmi < 18.5:
            weightbmi = ideal_weight - appoint.weight
        
        Weightbmi=round(weightbmi,2)

    

    

    if appoint.month8 == "JAN":
        month=1

    if appoint.month8 == "FEB":
        month=2

    if appoint.month8 == "MAR":
        month=3

    if appoint.month8 == "APR":
        month=4

    if appoint.month8 == "MAY":
        month=5

    if appoint.month8 == "JUN":
        month=6

    if appoint.month8 == "JUL":
        month=7

    if appoint.month8 == "AUG":
        month=8

    if appoint.month8 == "SEP":
        month=9

    if appoint.month8 == "OCT":
        month=10

    if appoint.month8 == "NOV":
        month=11

    if appoint.month8 == "DEC":
        month=12

    if appoint.year8 == "2019":
        year=2019

    if appoint.year8 == "2020":
        year=2020


    last_period_month=(date.today().year-year)*12+(date.today().month-month)

    

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
    print(appoint.medicalAllergies)
    context={
        "appoint":appoint,
        "age":age,
        "waist_hip":waist_hip,
        "weight_gained":weight_gained,
        "bmi":bmi,
        "pcos_ratio":pcos_ratio,
        "thyroid_ratio":thyroid_ratio,
        "prolac_ratio":prolac_ratio,
        "last_period_month":last_period_month,
        "Weightbmi":Weightbmi,
        
        
        
    }
    return render(request,'main/output.html',context)


def doctor_output(request):
    form = DoctorOutputForm()
    if request.method == 'POST':
        form =DoctorOutputForm(request.POST)
        if form.is_valid():
           
            form.save()
            print('valid')
            return redirect('/response')
        else:
            print('invalid')

    

    context={
        "form":form,
        
    }

    return render(request,'main/doctor_output.html',context)

def response(request):
    patiend_id=DoctorOutput.objects.all().last()

    email_id=patiend_id.patient_email

    if Patient.objects.filter(email=email_id).exists():
    
   
        appoint=Patient.objects.filter(email=email_id).first()
        

        if appoint.dob == None:
            age =""
        else:
            age = (date.today() - appoint.dob) // timedelta(days=365.2425)



        
        if appoint.weight == None or appoint.weight9 == None:
            weight_gained="n"
        else:
            weight_gain=(appoint.weight9/(appoint.weight-appoint.weight9))*100
            weight_gained=round(weight_gain,2)

        


        if appoint.waist == None or appoint.hip == None:
            waist_hip=0
        else:
            waisthip=appoint.waist/appoint.hip
            waist_hip=round(waisthip,2)



        if appoint.height_feet == None :
            height=0
        else:
            if appoint.height_inches == None:
                appoint.height_inches = 0
            height=(appoint.height_feet*30.48+appoint.height_inches*2.54)/100

        


        if appoint.weight == None or height == 0 :
            bmi=0
        else:
            BMI=appoint.weight/(height*height)
            bmi=round(BMI,2)




        if height == 0:
            ideal_weight=""
        else:
            ideal_weight=24.9*height*height

    

        
        weightbmi=0

        if bmi == 0:
            Weightbmi="n"

        else:

            if bmi >= 25:
                weightbmi = appoint.weight - ideal_weight

            elif bmi < 18.5:
                weightbmi = ideal_weight - appoint.weight
            
            Weightbmi=round(weightbmi,2)

        

        

        if appoint.month8 == "JAN":
            month=1

        if appoint.month8 == "FEB":
            month=2

        if appoint.month8 == "MAR":
            month=3

        if appoint.month8 == "APR":
            month=4

        if appoint.month8 == "MAY":
            month=5

        if appoint.month8 == "JUN":
            month=6

        if appoint.month8 == "JUL":
            month=7

        if appoint.month8 == "AUG":
            month=8

        if appoint.month8 == "SEP":
            month=9

        if appoint.month8 == "OCT":
            month=10

        if appoint.month8 == "NOV":
            month=11

        if appoint.month8 == "DEC":
            month=12

        if appoint.year8 == "2019":
            year=2019

        if appoint.year8 == "2020":
            year=2020


        last_period_month=(date.today().year-year)*12+(date.today().month-month)

        

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
        print(appoint.medicalAllergies)
        context={
            "appoint":appoint,
            "age":age,
            "waist_hip":waist_hip,
            "weight_gained":weight_gained,
            "bmi":bmi,
            "pcos_ratio":pcos_ratio,
            "thyroid_ratio":thyroid_ratio,
            "prolac_ratio":prolac_ratio,
            "last_period_month":last_period_month,
            "Weightbmi":Weightbmi,
            
            
            
        }
        return render(request,'main/output.html',context)
    
    else:
        context={}
        return render(request,'main/error.html',context)


   