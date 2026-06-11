from django import forms


class UserProfileForm(forms.Form):
    image = forms.FileField(label="User Profile Image")
