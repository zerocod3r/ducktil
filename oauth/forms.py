#!/usr/bin/env python
# encoding: utf-8


from django.contrib.auth.forms import forms
from django.forms import widgets


class RequireEmailForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    oauthid = forms.IntegerField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super(RequireEmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'placeholder': "email", "class": "form-control"})
