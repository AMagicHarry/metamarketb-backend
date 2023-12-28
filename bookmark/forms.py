from django import forms

from bookmark.models import BookmarkItem, BookmarkList
from config.library.forms import add_style


class ListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        add_style(self.fields)

    class Meta:
        model = BookmarkList
        fields = ['list_name', 'description', 'access_level']


class ItemForm(forms.ModelForm):
    site_name = forms.CharField(
        max_length=50,
        label='사이트 이름',
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )
    site_url = forms.URLField(
        label='URL',
        widget=forms.URLInput(
            attrs={'class': 'form-control mt-2'},
        ),
    )

    class Meta:
        model = BookmarkItem
        fields = ['site_name', 'site_url']
        # TODO: add validator
