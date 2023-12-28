from django.urls import path

from app_index.views import IndexTemplateView, login_test_user, PopupView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('index/', IndexTemplateView.as_view()),
    path('login-test-user/<int:num>/', login_test_user, name="login_test_user"),
    path('metamask/', PopupView.as_view(), name='popup_view'),
]
