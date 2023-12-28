from django.urls import path

from bookmark.views import ListCreateView, BookmarkListView, \
    ListUpdateView, ItemListView, ItemCreateView, ItemDeleteView, ItemDetailView, ItemUpdateView, \
    PublicBookmarkListView, PublicItemListView, ListDeleteView, register_favorite_list, delist_favorite_list, \
    register_favorite_item, delist_favorite_item, follow_user, unfollow_user
from config.library.views import custom_login_required
# ToDo: LoginRequiredMixin Redirect to login_success view

app_name = "bookmark"

urlpatterns = [
    path('', BookmarkListView.as_view(), name="index"),
    path('add/', ListCreateView.as_view(), name="add_list"),
    path('update/<int:pk>/', ListUpdateView.as_view(), name="update_list"),
    path('delete/<int:pk>/', ListDeleteView.as_view(), name="delete_list"),

    path('<int:pk>/', ItemListView.as_view(), name="item_list"),
    path('<int:pk>/add/', ItemCreateView.as_view(), name="add_item"),
    path('<int:list_pk>/delete/<int:pk>/', ItemDeleteView.as_view(), name="delete_item"),
    path('<int:list_pk>/detail/<int:pk>/', ItemDetailView.as_view(), name="item_detail"),
    path('<int:list_pk>/update/<int:pk>/', ItemUpdateView.as_view(), name="update_item"),

    path('<str:nickname>/', PublicBookmarkListView.as_view(), name='public_list'),
    path('<str:nickname>/<int:pk>/', PublicItemListView.as_view(), name='public_item_list'),
    path('<str:nickname>/<int:list_pk>/detail/<int:pk>/', ItemDetailView.as_view(), name="public_item_detail"),

    path('<str:nickname>/<int:pk>/like-this/', register_favorite_list, name="register_favorite_list"),
    path('<str:nickname>/<int:pk>/unlike-this/', delist_favorite_list, name="delist_favorite_list"),
    path('<str:nickname>/<int:list_pk>/<int:pk>/like-this/', register_favorite_item, name="register_favorite_item"),
    path('<str:nickname>/<int:list_pk>/<int:pk>/unlike-this/', delist_favorite_item, name="delist_favorite_item"),

    path('<str:nickname>/follow/', follow_user, name='follow_user'),
    path('<str:nickname>/unfollow/', unfollow_user, name="unfollow_user"),
]
