from django.contrib import admin
from main.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','weight','height_feet','height_inches','waist','hip','purpose','have_baby',
    'hyperprolactinemia','pcos_pcod','hypothyroidism','other','hyperprolactinemia_days','pcos_pcod_days','hypothyroidism_days','other_days','hyperprolactinemia_days_type','pcos_pcod_days_type','hypothyroidism_days_type','other_days_type','other_type',
    'symptoms7','month8','year8','weight9','time9','time9_d','stoppedPeriods','lessThanSixCycles','moreThanSixCycles','countinuosFlow',
    'currentlyNotUnderAnyMedication',
    'currentlyNotUnderAnyMedicationDuration',
    'currentlyNotUnderAnyMedicationDurationType',

    'diabestes',
    'diabestesDuration',
    'diabestesDurationType',

    'migrane',
    'migraneDuration',
    'migraneDurationType',

    'medicationHighBloodPressure',
    'medicationHighBloodPressureDuration',
    'medicationHighBloodPressureDurationType',

    'medicationMentalHealthDisorder',
    'medicationMentalHealthDisorderDuration',
    'medicationMentalHealthDisorderDurationType',

    'steroidTherapy',
    'steroidTherapyDuration',
    'steroidTherapyDurationType',

    'hormonalContraception',
    'hormonalContraceptionDuration',
    'hormonalContraceptionDurationType',

    'seizure',
    'seizureDuration',
    'seizureDurationType',

    'proteinSupplements',
    'proteinSupplementsDuration',
    'proteinSupplementsDurationType',

    'Opioids',
    'OpioidsDuration',
    'OpioidsDurationType',

    'antiHistamines',
    'antiHistaminesDuration',
    'antiHistaminesDurationType',

    'medicalAllergies',

    'undergoneSurgery',
    'physicallyImmobile',
    'viralFever',

    'workoutValue',
    'eatFoodValue',

    'sleepValue',
    

    'highBloodPressure',
    'highCholesterol',
    'familyHypothyroidism',
    'diabetes',
    'pcos',

    'reportFirst',
    'reportSecond',

    'otherExtraDetailForDoctor',

    'nutritionExpert',
    'yogaTherapist',
    'dermatologist',
    'psychiatrist',

    'hairLoss',
    'hairLossRange',
    'hairLossTime',
    'hairLossTimeType',

    'acneLoss',
    'acneLossRange',
    'acneLossTime',
    'acneLossTimeType',

    'missedPeriod',
    'missedPeriodTime',
    'missedPeriodTimeType',

    'extraHair',
    'extraHairRange',
    'extraHairTime',
    'extraHairTimeType',

    'constipation',

    'skinPigmentation',

    'slowHeartbeat',

    'headache',
    'headacheRange',
    'headacheTime',
    'headacheTimeType',

    'dischargeNipple',

    'moodSwings',

    'others',
    'othersRange',
    'othersTime',
    'othersTimeType',
    'symptoms10',




    


    ]

admin.site.register(
    Patient,
    PatientAdmin,
)
