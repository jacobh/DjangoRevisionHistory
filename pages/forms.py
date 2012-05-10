from django import forms
from pages.models import Page

class NewPageForm(forms.ModelForm):
	class Meta:
		model = Page
		exclude = ('parent',)