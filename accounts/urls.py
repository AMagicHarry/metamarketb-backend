from django.urls import path, reverse_lazy

from accounts.views import LoginView, LogoutView, logout_success, RegistrationView, register_success, \
    CustomPWChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from config.library.views import custom_user_passes_test, custom_login_required

app_name = 'accounts'

urlpatterns = [
    # path('', accounts_views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('logout-success/', logout_success, name="logout_success"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('register-success/', register_success, name="register_success"),

    path('password-change/', CustomPWChangeView.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
