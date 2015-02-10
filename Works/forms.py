from django import forms
from .models import category

class UploadWorkForm(forms.Form):
	title = forms.CharField(required=True,)
	description = forms.CharField(required=True,)
	category = forms.ChoiceField(choices=category,required=True,)
	archive = forms.FileField(required=True,)
	cover = forms.ImageField(required=True,)
