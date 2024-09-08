from django import forms
from . import models

class Contactform(forms.ModelForm):
    class Meta:
        model = models.Contactus
        fields = ['fullname', 'email', 'subject', 'nbre_de_place','description']  # Liste des champs du modèle

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-name', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'cf-email', 'placeholder': 'Enter Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'cf-subject', 'placeholder': 'Subject'}),
            'nbre_de_place': forms.NumberInput(attrs={'class': 'form-control', 'id': 'cf-nbre', 'placeholder': 'Combien de place désirez-vous ?'}),
            # 'rdv': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'id': 'cf-datetime'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'id': 'cf-description', 'placeholder': 'Tell Me Something'}),
        }
