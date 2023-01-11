from django import forms 
from django.contrib.auth import get_user_model


User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField()


class loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput
		)


class RegisterForm(forms.Form):
	username= forms.CharField()
	email= forms.EmailField()
	password= forms.CharField(widget=forms.PasswordInput)
	password2= forms.CharField(label='confirm password',widget=forms.PasswordInput)


	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		print(qs)
		if qs.exists():
			raise forms.ValidationError("Username is Taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs1 = User.objects.filter(email=email)
		print(qs1)
		if qs1.exists():
			raise forms.ValidationError("Email is Repeated")
		return email


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2= self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Password does not match.")
		return data