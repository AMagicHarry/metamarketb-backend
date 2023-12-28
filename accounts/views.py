from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import PWChangeForm, RegistrationForm, PWResetEmailForm, LoginForm, PWResetForm


# def index(request): # temporary
#    return HttpResponse('Hello')

class LoginForbiddenMixin(UserPassesTestMixin):
    # login_url = reverse_lazy('bookmark:index')

    def test_func(self):
        return not self.request.user.is_authenticated
        # ToDo: 403 에러 핸들러, alert('이미 로그인되어있습니다');


class LoginView(LoginForbiddenMixin, auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('accounts:logout_success')
    # ToDo: next_page LoginRequiredMixin에 활용


def logout_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/logout_success.html')
    # TODO: redirect


def register_success(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/register_success.html')
    # TODO: redirect


class RegistrationView(LoginForbiddenMixin, FormView):
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:register_success')
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomPWChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')
    form_class = PWChangeForm


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_success.html"


class PasswordResetView(LoginForbiddenMixin, auth_views.PasswordResetView):
    # ToDo: login_forbidden
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    template_name = 'accounts/password_reset_form.html'
    form_class = PWResetEmailForm


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'
    form_class = PWResetForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
