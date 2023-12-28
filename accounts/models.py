from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.apps import apps


class UsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w-]+\Z'
    message = _(
        '영문자, 숫자, - 또는 _만 사용 가능합니다.'
    )


class UserProfile(AbstractUser):
    def _upload_to(instance, filename): # ToDo: 업로드 하는 경로 유의하기
        return 'profile_images/%s/%s' % (instance.username, filename)

    username_validator = UsernameValidator()
    username = models.CharField(
        _('아이디'),
        max_length=36,
        unique=True,
        help_text= _('필수 항목. 36자 이하로 영문자, 숫자, - 또는 _만 사용 가능합니다.'),
        validators=[username_validator],
        error_messages={
            'unique': _("해당 아이디는 이미 존재합니다."),
        }
    )
    nickname = models.CharField(
        _('닉네임'),
        max_length=36,
        unique=True,
        help_text=_('필수 항목. 36자 이하로 영문자, 숫자, - 또는 _만 사용 가능합니다.'),
        validators=[username_validator],
        error_messages={
            'unique': _("해당 닉네임은 이미 존재합니다."),
        }
    )
    email = models.EmailField(_('이메일'), blank=True)

    name = models.CharField(_('이름'), max_length=15, blank=True)
    first_name = last_name = None

    birth_date = models.DateField(_('생년월일'), blank=True, null=True)
    belong_to = models.CharField(_('소속'), max_length=30, blank=True, null=True)

    profile_image = models.ImageField(_('프로필 이미지'), upload_to=_upload_to, default='profile_images/no_image.png')
    state_message = models.CharField(_('상태 메시지'), max_length=50, blank=True, null=True)

    favorite_lists = models.ManyToManyField('bookmark.BookmarkList', related_name="fan_of_list", blank=True)
    favorite_items = models.ManyToManyField('bookmark.BookmarkItem', related_name="fan_of_item", blank=True)

    # REQUIRED_FIELDS = [email]
    # username과 password는 required, AbstractUser에서는 email도

    def is_list_fan(self, _list_pk):
        BookmarkList = apps.get_model('bookmark.BookmarkList')
        _list = BookmarkList.objects.get(pk=_list_pk)
        if _list:
            if _list.fan_of_list.filter(pk=self.pk):
                return {
                    'list': _list,
                    'is_fan': True,
                }

        return None # ToDo: raise 404

    def is_item_fan(self, _item_pk):
        BookmarkItem = apps.get_model('bookmark.BookmarkItem')
        _item = BookmarkItem.objects.get(pk=_item_pk)
        if _item:
            if _item.fan_of_item.filter(pk=self.pk):
                return {
                    'item': _item,
                    'is_fan': True,
                }

        return None  # ToDo: raise 404

    def is_following(self, _owner_nickname):
        _owner = UserProfile.objects.filter(nickname=_owner_nickname).get()
        return self.following.filter(following=_owner).count()


class Follower(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='follower', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)
