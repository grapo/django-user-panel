from django import forms
from django.contrib.auth import get_user_model, _get_backends
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.Form):
    val = forms.CharField(label='User.{id,username,email}')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.user = None

    def get_user(self):
        return self.user

    def clean_val(self):
        val = self.cleaned_data['val']
        User = get_user_model()

        if '@' in val:
            auth = {'email': val}

        try:
            auth = {'pk': int(val)}
        except ValueError:
            auth = {'username': val}
        try:
            self.user = User.objects.get(**auth)
            backend, backend_path = _get_backends(return_tuples=True)[0]
            self.user.backend = backend_path
        except User.DoesNotExist:
            raise forms.ValidationError(_('User does not exist'))
        return val
