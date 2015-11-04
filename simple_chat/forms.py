#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, Textarea, Select, CheckboxInput, RadioSelect, DateInput, HiddenInput, EmailInput

from django.utils.translation import ugettext_lazy as _


class MessageForm(forms.Form):
    message = forms.Field(required=True, widget=forms.Textarea(attrs={"placeholder": _("Enter your message..."),
                                                                      "class": "form-control send-message",
                                                                      "rows": "3"}))
    name = forms.Field(required=True, widget=forms.TextInput(attrs={"placeholder": _("Your name"),
                                                                    "class": "form-control name-input pull-right"}))