# posts/forms.py
from django import forms
from .models import FaceFinder
 
class FaceFinderForm(forms.ModelForm):
 
    class Meta:
        model = FaceFinder
        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 35}),
        }
        
        fields = ['title', 'imageIn', 'videoIn']
        name = fields[0]
        image = fields[1]
        video = fields[2]
