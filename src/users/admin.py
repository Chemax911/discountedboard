from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm


User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):

    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User
    list_display = ['email', 'username', 'email_verify']
    list_editable = ('email_verify',)
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'email_verify', 'username', 'password1', 'password2'),
        }),
    )
