from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from accounts.models import UserProfile


class IndexTemplateView(TemplateView):
    template_name = 'app_index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['test_users'] = UserProfile.objects.filter(
            username__startswith='test')

        return context


def login_test_user(request, num):
    print(num)
    if num >= 1 and num <= 10:
        test_user = UserProfile.objects.get(username='test%03d' % (num))
        login(request, test_user)

        return redirect(reverse_lazy('bookmark:index'))


def read_file(request):
    file_path = '../file.txt'
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return render(request, 'templates/app_index/meta.html', {'file_contents': file_contents})


class PopupView(TemplateView):
    template_name = 'app_index/meta.html'
