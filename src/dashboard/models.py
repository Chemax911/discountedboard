from django.conf.urls.static import static
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NOT_SPECIFIED = 2

GENDER_CHOICES = (
	(GENDER_MALE, _('мужчина')),
	(GENDER_FEMALE, _('женщина')),
	(GENDER_NOT_SPECIFIED, _('не указано')),
)


class Profile(models.Model):
	# Managed fields
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='dashboard/profiles/avatars/', null=True, blank=True)
	gender = models.IntegerField(
		verbose_name=_('Пол'),
		choices=GENDER_CHOICES,
		default=GENDER_NOT_SPECIFIED)
	birthday = models.DateField(verbose_name=_('Дата рождения'), null=True, blank=True)
	description = models.TextField(verbose_name=_('Коротко о себе'))

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('Profile')
		verbose_name_plural = _('Profiles')

	def __str__(self):
		return str(self.user)

	@property
	def get_avatar(self):
		return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
