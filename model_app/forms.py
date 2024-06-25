from django import forms
from model_app.models import SpecialForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = SpecialForm
        fields = '__all__' 