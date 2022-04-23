from django import forms
from .models import Recycle

class RecycleForm(forms.ModelForm):

    class Meta:
        model = Recycle
        exclude = ('profile', 'date')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
