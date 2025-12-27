from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age','department', 'roll_number', 'year' ,'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),    
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 30:
            raise forms.ValidationError("Age must be between 10 to 30")
        return age
        
    def clean_roll_number(self):
        roll = self.cleaned_data.get('roll_number')
        if not roll.isdigit():
            raise forms.ValidationError("Roll number must contain only digits.")
        return roll