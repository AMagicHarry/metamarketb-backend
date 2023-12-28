from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from accounts.models import UserProfile


class BookmarkList(models.Model):
    user = models.ManyToManyField(UserProfile, related_name='own_list')

    list_name = models.CharField(_("리스트 이름"), max_length=50)
    description = models.CharField(_("설명"), max_length=255)

    ACCESS_LEVEL_CHOICES = (
        ('P', _('개인')),
        ('S', _('공개')),
    )
    access_level = models.CharField(
        _("접근 권한"),
        max_length=1,
        choices=ACCESS_LEVEL_CHOICES,
        default='P',
    )

    created_at = models.DateTimeField(_("생성 시간"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정 시간"), auto_now=True)

    def __str__(self):
        return '<' + self.list_name + '> ' + self.description


class BookmarkItem(models.Model):
    belonged_list = models.ForeignKey(BookmarkList, on_delete=models.CASCADE)

    site_name = models.CharField(_("사이트 이름"), max_length=50)
    site_url = models.URLField("URL")

    created_at = models.DateTimeField(_("생성 시간"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정 시간"), auto_now=True)

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse_lazy('bookmark:detail', args=[self.id])
        # TODO: CBV에서 처리할 수 있는 방법은 없는가 - get_success_url 오버라이딩
