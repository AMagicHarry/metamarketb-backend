from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from accounts.models import UserProfile, Follower
from bookmark.forms import ListForm, ItemForm
from bookmark.models import BookmarkItem, BookmarkList


class BookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/bookmark_list.html"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = BookmarkList.objects.filter(user=self.request.user)
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _user = self.request.user

        if _user.is_authenticated:
            context['follower_cnt'] = Follower.objects.filter(following=_user).count()

        return context



class ListCreateView(LoginRequiredMixin, CreateView): # ToDo: login success로 redirect
    model = BookmarkList
    template_name = 'bookmark/list_add.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        _is_valid = super(ListCreateView, self).form_valid(form)
        if _is_valid:
            _list = form.instance
            _list.user.set([self.request.user])

        return _is_valid


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkList
    template_name = 'bookmark/list_update.html'
    form_class = ListForm
    success_url = reverse_lazy('bookmark:index')


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model=BookmarkList,
    success_url=reverse_lazy('bookmark:index'),
    template_name='bookmark/list_confirm_delete.html',


class ItemListView(ListView):
    model = BookmarkItem
    template_name = "bookmark/item_list.html"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = BookmarkItem.objects.filter(belonged_list=self.kwargs['pk'])
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _user = self.request.user

        context['url_list_pk'] = self.kwargs.get('pk')
        if _user.is_authenticated:
            context['follower_cnt'] = Follower.objects.filter(following=_user).count()

        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = BookmarkItem
    template_name = 'bookmark/item_add.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('pk')],
        )

    def form_valid(self, form):
        list_pk = self.kwargs.get('pk')
        form.instance.belonged_list = BookmarkList.objects.get(pk=list_pk)
        return super(ItemCreateView, self).form_valid(form)


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = BookmarkItem
    template_name = 'bookmark/item_detail.html'


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkItem
    template_name = 'bookmark/item_update.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('pk')],
        )


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BookmarkItem
    template_name = 'bookmark/item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'bookmark:item_list',
            args=[self.kwargs.get('list_pk')],
        )


class PublicBookmarkListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_bookmark_list.html"
    paginate_by = 6

    def get_queryset(self):
        _user = UserProfile.objects.filter(nickname=self.kwargs.get('nickname')).get()
        if _user:
            queryset = get_list_or_404(BookmarkList, user=_user, access_level='S')
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _nickname = self.kwargs.get('nickname')
        _user = self.request.user
        _owner = UserProfile.objects.filter(nickname=_nickname).get()
        _list = context['object_list']

        context['follower_cnt'] = Follower.objects.filter(following=_owner).count()
        context['url_nickname'] = _nickname
        context['is_following'] = _user.is_following(_nickname)

        _is_list_fan = dict()
        for item in _list:
            _is_list_fan[item.pk] = _user.is_list_fan(item.pk)

        context['is_fan'] = _is_list_fan

        return context


class PublicItemListView(ListView):
    model = BookmarkList
    template_name = "bookmark/public_item_list.html"
    paginate_by = 6

    def get_queryset(self):
        _user = UserProfile.objects.filter(nickname=self.kwargs.get('nickname')).get()
        if _user:
            _list = get_object_or_404(
                BookmarkList,
                user=_user,
                access_level='S',
                id=self.kwargs.get('pk')
            )
            queryset = _list.bookmarkitem_set.all()
            return queryset
        else:
            # TODO: 임시 방편
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _nickname = self.kwargs.get('nickname')
        _user = self.request.user

        context['url_list_pk'] = self.kwargs.get('pk')
        context['url_nickname'] = self.kwargs.get('nickname')
        context['is_following'] = _user.is_following(_nickname)

        return context


def register_favorite_list(request, **kwargs):
    if request.method == "POST":
        user = request.user
        _list = get_object_or_404(BookmarkList, pk=request.POST['list_pk'])

        if _list.user.get() != user:
            _list.fan_of_list.add(user)

            return JsonResponse({
                'cnt': _list.fan_of_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'register 안돼요'},
        status=500
    )


def delist_favorite_list(request, **kwargs):
    if request.method == "POST":
        user = request.user
        result = user.is_list_fan(request.POST['list_pk'])

        if result and result['is_fan']:
            fan_list = result['list'].fan_of_list
            fan_list.remove(user)

            return JsonResponse({
                'cnt': fan_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'delist 실패'},
        status=500
    )

def register_favorite_item(request, **kwargs):
    if request.method == "POST":
        user = request.user
        _item = get_object_or_404(BookmarkItem, pk=request.POST['item_pk'])

        if _item.belonged_list.user.get() != user:
            _item.fan_of_item.add(user)

            return JsonResponse({
                'cnt': _item.fan_of_item.count()
            })

    return JsonResponse(
        {'status':'false','message': 'register 안돼요'},
        status=500
    )


def delist_favorite_item(request, **kwargs):
    if request.method == "POST":
        user = request.user
        result = user.is_item_fan(request.POST['item_pk'])

        if result and result['is_fan']:
            fan_list = result['item'].fan_of_item
            fan_list.remove(user)

            return JsonResponse({
                'cnt': fan_list.count()
            })

    return JsonResponse(
        {'status':'false','message': 'delist 실패'},
        status=500
    )


def follow_user(request, nickname):
    _user = request.user
    if request.method == "POST" and _user.nickname != nickname:
        if not _user.is_following(nickname):
            _followed = UserProfile.objects.filter(nickname=nickname).get()

            print(_followed.nickname)

            follow = Follower(following=_followed, follower=_user)
            follow.save()

            return JsonResponse({
                'cnt': Follower.objects.filter(following=_followed).count()
            })

    return JsonResponse(
        {'status': 'false', 'message': 'follow 실패'},
        status=500
    )


def unfollow_user(request, nickname):  # ToDo: 코드 형식이 너무 비슷해 보임, 실패 메시지 제대로
    _user = request.user
    if request.method == "POST":
        if _user.is_following(nickname):
            _followed = UserProfile.objects.filter(nickname=nickname).get()

            follow = Follower.objects.filter(following=_followed, follower=_user)
            follow.delete()

            return JsonResponse({
                'cnt': Follower.objects.filter(following=_followed).count()
            })

    return JsonResponse(
        {'status': 'false', 'message': 'unfollow 실패'},
        status=500
    )
