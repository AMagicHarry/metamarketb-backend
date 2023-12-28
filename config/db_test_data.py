import random
import time

from accounts.models import UserProfile, Follower
from bookmark.models import BookmarkList, BookmarkItem


# run this in django console
# execfile('config/db_test_data.py)


class UserManager:
    cnt = 10
    user_data = [
        {
            'username': "test%03d" % (i),
            'nickname': "test_%03d" % (i),
            'email': "test%03d@naver.com" % (i),
            'name': "Tester_%03d" % (i),
            'birth_date': '2019-06-24',
            'belong_to': "Test",
            'state_message': "Tester_%03d is ready!!!" % (i),
        } for i in range(1, cnt+1)
    ]
    users = []

    @classmethod
    def create_users(cls):
        for data in cls.user_data:
            user = UserProfile()
            user.username = data['username']
            user.nickname = data['nickname']
            user.email = data['email']
            user.name = data['name']
            user.birth_date = data['birth_date']
            user.belong_to = data['belong_to']
            user.state_message = data['state_message']

            user.save()

            cls.users.append(user)

        print('create_users: success!!!')

    @classmethod
    def delete_users(cls):
        if cls.users:
            for user in cls.users:
                user.delete()
        else:
            for data in cls.user_data:
                user = UserProfile.objects.filter(username=data['username']).get()
                user.delete()

        print('delete_users: success!!!')

    @classmethod
    def get_users(cls):
        for data in cls.user_data:
            cls.users.append(
                UserProfile.objects.filter(username=data['username']).get()
            )


class ListManager:
    cnt = 200
    _list_data = [
        {
            'username': "test%03d" % (random.randrange(1, UserManager.cnt+1)),
            'list_name': "test%05d" % (i),
            'description': 'test data...',
            'access_level': 'P' if random.randrange(0, 2) else 'S',
        } for i in range(1, cnt + 1)
    ]
    _lists = []

    @classmethod
    def create_lists(cls):
        for data in cls._list_data:
            _list = BookmarkList(
                list_name=data['list_name'],
                description=data['description'],
                access_level=data['access_level'],
            )

            _list.save()
            _list.user.add(UserProfile.objects.filter(username=data['username']).get())
            _list.save()

            cls._lists.append(_list)

        print('create_lists: sucess!!')

    @classmethod
    def delete_lists(cls):
        if cls._lists:
            for _list in cls._lists:
                _list.delete()
        else:
            for data in cls._list_data:
                _list = BookmarkList.objects.filter(list_name=data['list_name'])
                _list.delete()

        print('delete_lists: sucess!!')

    @classmethod
    def get_lists(cls):
        for data in cls._list_data:
            cls._lists.append(
                BookmarkList.objects.filter(list_name=data['list_name']).get()
            )


class ItemManager:
    cnt = 1000
    item_data = [
        {
            'belonged_list_name': "test%05d" %(random.randrange(1, ListManager.cnt+1)),
            'site_name': 'test%05d' % (i),
            'site_url': 'http://google.com/#test%05d' % (i),
        } for i in range(1, cnt+1)
    ]
    items = []

    @classmethod
    def create_items(cls):
        for data in cls.item_data:
            item = BookmarkItem(
                site_name=data['site_name'],
                site_url=data['site_url'],
            )

            item.belonged_list = BookmarkList.objects.filter(list_name=data['belonged_list_name']).get()
            item.save()

            cls.items.append(item)

        print('create_items: success!!!')

    @classmethod
    def delete_items(cls):
        if cls.items:
            for item in cls.items:
                item.delete()
        else:
            for data in cls.item_data:
                item = BookmarkItem.objects.filter(site_name=data['site_name']).get()
                item.delete()

        print('delete_items: success!!!')

    @classmethod
    def get_items(cls):
        for data in cls.item_data:
            item = BookmarkItem.objects.filter(site_name=data['site_name']).get()
            cls.items.append(
                item
            )


class BaseFavoriteFieldManager:
    ratio = 0.7
    _field = None
    _manager_class = None

    @classmethod
    def create_favorites(cls):
        if cls._field == 'favorite_lists':
            for user in UserManager.users:
                for i in range(0, int(ListManager.cnt * cls.ratio)):
                    user.favorite_lists.add(
                        ListManager._lists[random.randrange(0, cls._manager_class.cnt)]
                    )
        elif cls._field == 'favorite_items':
            for user in UserManager.users:
                for i in range(0, int(ItemManager.cnt * cls.ratio)):
                    user.favorite_items.add(
                        ItemManager.items[random.randrange(0, cls._manager_class.cnt)]
                    )

        print('create_' + cls._field + ': success!!!')

    @classmethod
    def delete_favorites(cls):
        if cls._field == 'favorite_lists':
            for user in UserManager.users:
                user.favorite_lists.all().delete()
        elif cls._field == 'favorite_items':
            for user in UserManager.users:
                user.favorite_items.all().delete()

        print('delete_' + cls._field + ': success!!!')


class FavoriteListManager(BaseFavoriteFieldManager):
    _field = 'favorite_lists'
    _manager_class = ListManager


class FavoriteItemManager(BaseFavoriteFieldManager):
    _field = 'favorite_items'
    _manager_class = ItemManager


class FollowerManager:
    ratio = 0.4

    @classmethod
    def create_followers(cls):
        for user in UserManager.users:
            for i in range(0, int(UserManager.cnt * cls.ratio)):
                idx = random.randint(0, UserManager.cnt-1)
                while user == UserManager.users[idx] \
                        or user.is_following(UserManager.users[idx].nickname) :
                    idx = random.randint(0, UserManager.cnt-1)

                followed = UserManager.users[idx]

                follow = Follower(following=followed, follower=user)
                follow.save()

        print('create_followers: success!!!')

    @classmethod
    def delete_followers(cls):
        pass


def main():
    # ToDo: check the insertData time

    UserManager.create_users()
    ListManager.create_lists()
    ItemManager.create_items()

    #UserManager.get_users()
    #ListManager.get_lists()
    #ItemManager.get_items()

    FavoriteListManager.create_favorites()
    FavoriteItemManager.create_favorites()

    FollowerManager.create_followers()

    #time.sleep(100)

    #UserManager.delete_users()

    #ListManager.delete_lists()
    #ItemManager.delete_items()

    #FavoriteListManager.delete_favorites()
    #FavoriteItemManager.delete_favorites()

    following = {
    }
    follower = {
    }


main()
