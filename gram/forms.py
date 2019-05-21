from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']











# from django import forms
# from .models import *



# class ProfileForm(forms.ModelForm):
#     class Meta:
#         bio = forms.CharField(label = "Bio")
#         pic = forms.ImageField(label = "Pic")


# class ImageForm(forms.ModelForm):
#     # image_url = forms.ImageField(label='Picture')
#     class Meta:
#         model = Image
#         exclude = ('user',)


# # class RegistrationForm(forms.ModelForm):
# #     class Meta:
# #        model = RegistrationForm
# #        exclude = ('user',)


        