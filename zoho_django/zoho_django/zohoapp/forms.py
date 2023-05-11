from django import forms
from zohoapp.models import MyForm
class employeeforms(forms.ModelForm):  
    class Meta:
        model = MyForm
        fields = '__all__'