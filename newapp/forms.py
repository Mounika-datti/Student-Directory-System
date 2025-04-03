from django import forms
from .models import Student

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone'] # Remove 'address' from this list
        widgets = {
            'roll_no': forms.TextInput(attrs={'readonly': 'readonly'}),
        }