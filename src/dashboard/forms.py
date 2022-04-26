from django import forms

from src.dashboard.models import Profile


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.label = False
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'autocomplete': 'current-password'})
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['birthday'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control'})


# def form_validation_error(form):
#     """
#     Form Validation Error
#     If any error happened in your form, this function returns the error message.
#     """
#     msg = ""
#     for field in form:
#         for error in field.errors:
#             msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
#     return msg
