from django import forms
from .models import Teacher

class teacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','department','designation']


    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name and len(name) < 5:
            raise forms.ValidationError("Name must be at least 5 characters long.")
            
        return name
