from movieFormApp.models import Movie
from django import forms

class movieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

