from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (
	UserCreationForm as UserCreation,
	UserChangeForm as UserChange,
	PasswordResetForm as PasswordReset,
	AuthenticationForm as Authentication
)
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from src.users.utils import send_email_for_verify

User = get_user_model()


class AuthenticationForm(Authentication):
	""" User Authentication Form """

	class Meta:
		model = get_user_model
		fields = ('email', 'username', 'email_verify')

	def __init__(self, *args, **kwargs):
		super(AuthenticationForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.label = False
		self.fields['username'].widget.attrs.update({
			'class': 'form-control bdr'})
		self.fields['password'].widget.attrs.update({
			'class': 'form-control bdr'})

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		email_verify = self.cleaned_data.get('email_verify')

		if username is not None and password:
			self.user_cache = authenticate(
				self.request,
				username=username,
				password=password,
				email_verify=email_verify
			)
			if not self.user_cache.email_verify:
				send_email_for_verify(self.request, self.user_cache)
				raise ValidationError(
					_('Email not verify, check your email'),
					code='invalid_login'
				)

			if self.user_cache is None:
				raise self.get_invalid_login_error()
			else:
				self.confirm_login_allowed(self.user_cache)

		return self.cleaned_data


class UserAdminCreationForm(UserCreation):
	""" User Admin Creation Form """

	email = forms.EmailField(
		label=_('Email'), max_length=254,
		widget=forms.EmailInput(
			attrs={'autocomplete': 'email'}))

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')


class UserAdminChangeForm(UserChange):
	""" User Admin Change Form """

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')


class UserCreationForm(UserCreation):
	""" User Creation Form """

	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control bdr',
				'autocomplete': 'email'
			}))

	class Meta(UserCreation.Meta):
		model = get_user_model()
		fields = ('email', 'username')

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.label = False
		self.fields['username'].widget.attrs.update({
			'class': 'form-control bdr'})
		self.fields['password1'].widget.attrs.update({
			'class': 'form-control bdr'})
		self.fields['password2'].widget.attrs.update({
			'class': 'form-control bdr'})


class PasswordResetForm(PasswordReset):
	""" User Password Reset Form """

	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control bdr',
				'autocomplete': 'email'
			}))
