from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'mean_score']
        labels = {
            'student_number': 'Student Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'field_of_study' : 'Field of Study',
            'mean_score' : 'Mean Score'
        }
        widgets = {
        'student_number': forms.NumberInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name' :forms.TextInput(attrs={'class':'form-control'}),
        'email' :forms.EmailInput(attrs={'class':'form-control'}),
        'field_of_study' :forms.TextInput(attrs={'class':'form-control'}),
        'mean_score' : forms.NumberInput(attrs={'class':'form-control'}),
            
    }    