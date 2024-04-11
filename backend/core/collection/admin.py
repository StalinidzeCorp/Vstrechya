from django.contrib import admin
from .models import *
# Register your models here.


class MuseumCollectionInline(admin.TabularInline):
    model = MuseumCollection
    fields = ('collection', 'created_at')

    readonly_fields = ('id', 'created_at', 'collection', 'museum')
    can_delete = True
    max_num = 0
    extra = 0
    show_change_link = True


class MuseumCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'museum', 'collection', 'created_at')
    list_display_links = ('id', 'museum',)
    list_filter = ('museum',)
    search_fields = ('id', 'museum')
    readonly_fields = ('id', 'created_at', 'updated_at')


class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    fields = ('image_url', 'created_at', 'updated_at')

    readonly_fields = ('id', 'created_at', 'updated_at')
    can_delete = True
    max_num = 0
    extra = 0
    show_change_link = True


class CollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionItemInline]


admin.site.register(Collection, CollectionAdmin)
admin.site.register(UserCollection)
admin.site.register(CollectionItem)
admin.site.register(MuseumCollection, MuseumCollectionAdmin)
