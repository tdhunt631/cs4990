from django import forms

class ItemForm(forms.Form):
	name = forms.CharField(max_length=200)
	description = forms.CharField(max_length=200)
	quantity = forms.IntegerField()
