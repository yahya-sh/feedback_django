from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(min_length=3)
    feedback = forms.CharField(max_length=150, widget=forms.Textarea)
    rating = forms.IntegerField(max_value=5, min_value=1)
