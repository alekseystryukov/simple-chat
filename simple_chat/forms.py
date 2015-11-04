from django import forms
from django.utils.translation import ugettext_lazy as _


class MessageForm(forms.Form):
    """
    Chat message send form
    """
    message = forms.Field(required=True, widget=forms.Textarea(attrs={"placeholder": _("Enter your message..."),
                                                                      "class": "form-control send-message",
                                                                      "rows": "3"}))
    name = forms.Field(required=True, widget=forms.TextInput(attrs={"placeholder": _("Your name"),
                                                                    "class": "form-control name-input pull-right"}))