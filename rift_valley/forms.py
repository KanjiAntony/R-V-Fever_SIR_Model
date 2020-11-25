from django import forms

# creating a form
class InputForm(forms.Form):

	start_day = forms.CharField(label="start_day",max_length=100)

