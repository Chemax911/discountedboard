from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
	"""
	Abstract User Model
	"""

	username = models.CharField(
		_('username'),
		max_length=150,
		unique=False,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		error_messages={
			'unique': _("A user with that username already exists."),
		},
	)
	email = models.EmailField(_('Email address'), unique=True)
	email_verify = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
