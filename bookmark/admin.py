from django.contrib import admin

from bookmark.models import BookmarkItem, BookmarkList


class ItemInline(admin.StackedInline):
    model = BookmarkItem
    extra = 3


class ListAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [ItemInline]


admin.site.register(BookmarkList, ListAdmin)
admin.site.register(BookmarkItem)