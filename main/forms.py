from django import forms
from main.models import Patient,DoctorOutput

class PatientForm(forms.ModelForm):
    class Meta:
        model =Patient
        fields='__all__'

class DoctorOutputForm(forms.ModelForm):
    class Meta:
        model = DoctorOutput
        fields='__all__'

class FooterForm(forms.Form):
    f_email=forms.EmailField()