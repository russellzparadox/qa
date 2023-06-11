from django import forms

class question_form(forms.Form):
    text = forms.CharField(max_length=3000)
