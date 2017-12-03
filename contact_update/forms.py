from django import forms


class SearchForm(forms.Form):
    year = forms.DateField(input_formats=['%Y'])
    username = forms.CharField(min_length=2, max_length=32, strip=True)
    realname = forms.CharField(min_length=1, max_length=32, strip=True)
