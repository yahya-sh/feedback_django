from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(min_length=3)

