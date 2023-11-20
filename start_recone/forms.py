from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label='> Enter URL', max_length=200)