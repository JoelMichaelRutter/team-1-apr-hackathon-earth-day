from django import forms
from crispy_forms.helper import FormHelper

from .models import UserProfile

class UserProfileImageForm(forms.ModelForm):
    """
    Form to allow user to upload image
    """
    class Meta:
        model = UserProfile
        fields = ['image', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userProfileImageForm'
