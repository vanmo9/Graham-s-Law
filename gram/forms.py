from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField


class ProfileForm(forms,ModelsForm):
    class Meta:
        bio = forms.CharField(label = "Bio")
        pic = ImageField(label = "Pic")


class ImageForm(forms.ModelForm):
    image_url = ImageField(label='Picture')
    class Meta:
        model = Image
        fields = ("image_url","name","caption")