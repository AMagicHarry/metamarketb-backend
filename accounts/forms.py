from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.utils.translation import gettext_lazy as _

from accounts.models import UserProfile
from config.library.forms import add_style


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=36,
        label=_('아이디'),
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )
    password = forms.CharField(
        label=_('비밀번호'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mt-2'},
        )
    )

    error_messages = {
        'invalid_login': _(
            "아이디나 비밀번호를 확인해주세요"
        ),
        'inactive': _("이 계정은 사용정지 되었습니다"),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        # TODO: 이거 왜 그런거지? - AuthForm이 이미 request를 가지고 있다고 본거 같기도

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        # TODO: add validator


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        add_style(self.fields)

    class Meta:
        model = UserProfile
        fields = ('username', 'nickname', 'email', 'password1', 'password2', 'name',
                    'birth_date', 'belong_to', 'state_message', 'profile_image')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class PWChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        add_style(self.fields)


class PWResetEmailForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        add_style(self.fields)

        email = self.fields['email']
        email.label = '이메일'
        email.help_text = \
            '아래의 이메일로 안내 메시지가 전송됩니다. '\
            '회원가입 시 입력한 이메일을 입력해주세요.'


class PWResetForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        add_style(self.fields)
