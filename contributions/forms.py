from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Recycle, Reduce, Reuse

class RecycleForm(forms.ModelForm):
    """
    Form to add Recycle Action
    """
    class Meta:
        model = Recycle
        exclude = ('profile', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-recycleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_recycle'
        self.helper.add_input(Submit('submint', 'Submit'))


class ReduceForm(forms.ModelForm):
    """
    Form to add Reduce Action
    """
    class Meta:
        model = Reduce
        exclude = ('profile', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-reduceForm'


class ReuseForm(forms.ModelForm):
    """
    Form to add Reuse Action
    """
    class Meta:
        model = Reuse
        exclude = ('profile', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-reuseForm'
