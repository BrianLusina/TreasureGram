from django import forms
from .models import Treasures


# using meta class
class TreasureForm(forms.ModelForm):
    """
    Links a form to a model, the class will always be Meta and will be used to link form to the model
    The HTML form will display labels and input fields for these five fields
    """
    class Meta:
        model = Treasures
        fields = ['name', 'value', 'material', "location", "image"]


# subclassing form to Form class
# class TreasureForm(forms.Form):
#     name = forms.CharField(label="Name", max_length=100)
#     value = forms.DecimalField(label="Value", max_digits=10, decimal_places=2)
#     material = forms.CharField(label="Material", max_length=100)
#     location = forms.CharField(label="Location", max_length=100)
#     img_url = forms.CharField(label="Image URL", max_length=300)


# login form
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=84)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    """
    Sign up form
    """
    username = forms.CharField(label="Username", max_length=84)
    password = forms.CharField(forms.PasswordInput())
    retype_pass = forms.CharField(forms.PasswordInput())