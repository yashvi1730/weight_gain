from django.db import models


# Create your models here.
PURPOSE_CHOICES= (
    ('GW','I want to know why I might have gained weight'),
    ('FR','I am more concerned about future risks from this weight gain '),
    ('BC','Want to prepare my body for conception'),
    ('PR','Need to get my prescription renewed'),
    ('SO','Need to get a second opinion'),
    ('PC','Follow up for previous consultation'),
    ('other','Other')
)
HAVE_BABY_CHOICES=(
    ('y','yes'),
    ('n','no'),
)

YN_CHOICES=(
    ('y','yes'),
    ('n','no'),
)

MONTH8_CHOICES=(
    ('JAN','JAN'),
    ('FEB','FEB'),
    ('MAR','MAR'),
    ('APR','APR'),
    ('MAY','MAY'),
    ('JUN','JUN'),
    ('JUL','JUL'),
    ('AUG','AUG'),
    ('SEP','SEP'),
    ('OCT','OCT'),
    ('NOV','NOV'),
    ('DEC','DEC'),
)

YEAR8_CHOICES=(
    ('2019','2019'),
    ('2020','2020'),
)

TIME9_D_CHOICES=(
    ('d','days'),
    ('m','months'),
    ('y','years')
)
class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(default="2020-06-02")
    weight=models.IntegerField(default="50")
    height_feet=models.IntegerField(null=True,blank=True,default=0)
    height_inches=models.IntegerField(null=True,blank=True,default=0)
    waist=models.IntegerField(default="28")
    hip=models.IntegerField(default="30")
    purpose=models.CharField(max_length=100, choices=PURPOSE_CHOICES, default='None')
    have_baby=models.CharField(max_length=100,choices=HAVE_BABY_CHOICES,default='n')

    hyperprolactinemia=models.CharField(max_length=100,default='false',null=True,blank=True)
    pcos_pcod=models.CharField(max_length=100,default='false',null=True,blank=True)
    hypothyroidism=models.CharField(max_length=100,default='false',null=True,blank=True)
    other=models.CharField(max_length=100,default='false',null=True,blank=True)
    hyperprolactinemia_days=models.IntegerField(null=True,blank=True,default=0)
    pcos_pcod_days=models.IntegerField(null=True,blank=True,default=0)
    hypothyroidism_days=models.IntegerField(null=True,blank=True,default=0)
    other_days=models.IntegerField(null=True,blank=True,default=0)
    hyperprolactinemia_days_type=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    pcos_pcod_days_type=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    hypothyroidism_days_type=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    other_days_type=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    other_type=models.CharField(max_length=100,default='None',null=True,blank=True)
    



    symptoms7=models.CharField(max_length=100,default='None',null=True,blank=True)
    month8=models.CharField(max_length=100,choices=MONTH8_CHOICES,default='JAN')
    year8=models.CharField(max_length=100,choices=YEAR8_CHOICES,default='2019')
    weight9=models.IntegerField(null=True,blank=True,default=None)
    time9=models.IntegerField(null=True,blank=True,default=None)
    time9_d=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    stoppedPeriods=models.CharField(max_length=100,null=True,blank=True,default='false')
    lessThanSixCycles=models.CharField(max_length=100,null=True,blank=True,default='false')
    moreThanSixCycles=models.CharField(max_length=100,null=True,blank=True,default='false')
    countinuosFlow=models.CharField(max_length=100,null=True,blank=True,default='false')
    lastPeriodTimeMonth=models.CharField(max_length=100,choices=MONTH8_CHOICES,default='JAN')
    lastPeriodTimeYear=models.CharField(max_length=100,choices=YEAR8_CHOICES,default='2019')

    currentlyNotUnderAnyMedication=models.CharField(max_length=100,null=True,blank=True,default='false')
    diabestes=models.CharField(max_length=100,null=True,blank=True,default='false')
    migrane=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationHighBloodPressure=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationMentalHealthDisorder=models.CharField(max_length=100,null=True,blank=True,default='false')
    steroidTherapy=models.CharField(max_length=100,null=True,blank=True,default='false')
    hormonalContraception=models.CharField(max_length=100,null=True,blank=True,default='false')
    seizure=models.CharField(max_length=100,null=True,blank=True,default='false')
    proteinSupplements=models.CharField(max_length=100,null=True,blank=True,default='false')
    Opioids=models.CharField(max_length=100,null=True,blank=True,default='false')
    antiHistamines=models.CharField(max_length=100,null=True,blank=True,default='false')

    currentlyNotUnderAnyMedicationDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    diabestesDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    migraneDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationHighBloodPressureDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationMentalHealthDisorderDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    steroidTherapyDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    hormonalContraceptionDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    seizureDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    proteinSupplementsDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    OpioidsDuration=models.CharField(max_length=100,null=True,blank=True,default='false')
    antiHistaminesDuration=models.CharField(max_length=100,null=True,blank=True,default='false')

    currentlyNotUnderAnyMedicationDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    diabestesDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    migraneDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    medicationHighBloodPressureDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    medicationMentalHealthDisorderDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    steroidTherapyDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    hormonalContraceptionDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    seizureDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    proteinSupplementsDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    OpioidsDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    antiHistaminesDurationType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    
    medicalAllergies=models.CharField(max_length=100,null=True,blank=True,default='none')

    undergoneSurgery=models.CharField(max_length=100,null=True,blank=True,default='false')
    physicallyImmobile=models.CharField(max_length=100,null=True,blank=True,default='false')
    viralFever=models.CharField(max_length=100,null=True,blank=True,default='false')

    workoutValue=models.CharField(max_length=100,choices=YN_CHOICES,default='n')
    eatFoodValue=models.CharField(max_length=100,choices=YN_CHOICES,default='n')

    sleepValue=models.IntegerField(null=True,blank=True,default=0)
    

    highBloodPressure=models.CharField(max_length=100,null=True,blank=True,default='false')
    highCholesterol=models.CharField(max_length=100,null=True,blank=True,default='false')
    familyHypothyroidism=models.CharField(max_length=100,null=True,blank=True,default='false')
    diabetes=models.CharField(max_length=100,null=True,blank=True,default='false')
    pcos=models.CharField(max_length=100,null=True,blank=True,default='false')

    reportFirst =models.FileField(default='none')
    reportSecond =models.FileField(default='none')

    otherExtraDetailForDoctor=models.CharField(max_length=100,null=True,blank=True,default='none')

    nutritionExpert=models.CharField(max_length=100,null=True,blank=True,default='false')
    yogaTherapist=models.CharField(max_length=100,null=True,blank=True,default='false')
    dermatologist=models.CharField(max_length=100,null=True,blank=True,default='false')
    psychiatrist=models.CharField(max_length=100,null=True,blank=True,default='false')
    

    hairLoss=models.CharField(max_length=100,null=True,blank=True,default='false')
    hairLossRange=models.IntegerField(null=True,blank=True,default=None)
    hairLossTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    hairLossTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')

    acneLoss=models.CharField(max_length=100,null=True,blank=True,default='false')
    acneLossRange=models.IntegerField(null=True,blank=True,default=None)
    acneLossTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    acneLossTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')

    missedPeriod=models.CharField(max_length=100,null=True,blank=True,default='false')
    missedPeriodTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    missedPeriodTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')

    extraHair=models.CharField(max_length=100,null=True,blank=True,default='false')
    extraHairRange=models.IntegerField(null=True,blank=True,default=None)
    extraHairTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    extraHairTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')

    constipation=models.CharField(max_length=100,null=True,blank=True,default='false')

    skinPigmentation=models.CharField(max_length=100,null=True,blank=True,default='false')

    slowHeartbeat=models.CharField(max_length=100,null=True,blank=True,default='false')

    headache=models.CharField(max_length=100,null=True,blank=True,default='false')
    headacheRange=models.IntegerField(null=True,blank=True,default=None)
    headacheTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    headacheTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')

    dischargeNipple=models.CharField(max_length=100,null=True,blank=True,default='false')

    moodSwings=models.CharField(max_length=100,null=True,blank=True,default='false')

    others=models.CharField(max_length=100,null=True,blank=True,default='false')
    othersRange=models.IntegerField(null=True,blank=True,default=None)
    othersTime=models.CharField(max_length=100,null=True,blank=True,default='false')
    othersTimeType=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')




    
    
    


