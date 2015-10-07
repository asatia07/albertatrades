from django import forms
from django.forms import extras
from django.utils.translation import ugettext, ugettext_lazy as _


class FeedbackForm(forms.Form):
  """ feedback form """
  name = forms.CharField(label=_("Name"), required=True)
  email = forms.EmailField(label=_("Email"), required=True)
  feedback = forms.CharField(label=_("Feedback"), required=True, widget=forms.Textarea)
