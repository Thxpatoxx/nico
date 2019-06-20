from django import forms

from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):

    class Meta:
        model = Diagnostico
        fields = ('title', 'text',)