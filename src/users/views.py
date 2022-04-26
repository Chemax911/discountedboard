from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import (
	LoginView as Login,
	PasswordResetView as PasswordReset,
	PasswordResetConfirmView as PasswordResetConfirm
)
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View, generic

from src.users.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from src.users.utils import send_email_for_verify

User = get_user_model()


class LoginView(Login):
	""" User login page view """

	form_class = AuthenticationForm
	template_name = 'registration/login.html'


class EmailVerifyView(View):
	"""
	User verification email page view
	"""

	def get(self, request, uidb64, token):
		user = self.get_user(uidb64)

		if user is not None and token_generator.check_token(user, token):
			user.email_verify = True
			user.save()
			login(request, user)
			return redirect('home_view')

		return redirect('invalid_verify')

	@staticmethod
	def get_user(uidb64):
		try:
			uid = urlsafe_base64_decode(uidb64).decode()
			user = User.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
			user = None
		return user


class SignupPageView(generic.CreateView):
	"""
	User signup page view
	"""

	form_class = UserCreationForm
	success_url = reverse_lazy('home_view')
	template_name = 'registration/signup.html'

	def get(self, request, *args, **kwargs):
		context = {
			'form': UserCreationForm()}
		return super().get(
			request, self.template_name, context, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			user = authenticate(email=email, password=password)
			send_email_for_verify(request, user)
			return redirect('confirm_email')

		context = {'form': form}
		return super().post(
			request, self.template_name, context, *args, **kwargs)


class PasswordResetView(PasswordReset):
	"""
	User password reset page view
	"""

	# email_template_name = 'registration/password_reset_email.html'
	form_class = PasswordResetForm
	# subject_template_name = 'registration/password_reset_subject.txt'
	template_name = 'registration/password_reset_form.html'


class PasswordResetConfirmView(PasswordResetConfirm):
	"""
	User password reset confirm page view
	"""

	# form_class = SetPasswordForm
	template_name = 'registration/password_reset_confirm.html'
