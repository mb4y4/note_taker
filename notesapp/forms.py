# forms.py
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Write your thoughts',
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
        #if 'Django' not in title:
            raise forms.ValidationError('Input a longer Title')
        return title