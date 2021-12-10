from django import forms
from .models import Boardgame, Info

class GameForm(forms.ModelForm):

    class Meta:
        model = Boardgame
        fields = ['text']
        labels = {'text': ''}

class InfoForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = ['text']
        labels = {'text': 'Info:'}
        widgets = {'text': forms.Textarea(attrs={'cols' : 80})}