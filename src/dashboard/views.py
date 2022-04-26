from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views import View

from src.dashboard.forms import ProfileForm # form_validation_error
from src.dashboard.models import Profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
	profile = None

	def dispatch(self, request, *args, **kwargs):
		self.profile, __ = Profile.objects.get_or_create(user=request.user)
		return super(ProfileView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		context = {'profile': self.profile}
		return render(request, 'dashboard/profile.html', context)

	def post(self, request):
		form = ProfileForm(request.POST, request.FILES, instance=self.profile)

		if form.is_valid():
			profile = form.save()

			# to save user model info
			profile.user.username = form.cleaned_data.get('username')
			profile.user.email = form.cleaned_data.get('email')
			profile.user.save()

			messages.success(request, _('Profile saved successfully'))
		else:
			messages.error(request, form_validation_error(form))
		return redirect('profile')
