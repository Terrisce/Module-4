from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'description', 'price', 'created_date', 'negotiable', 'updated_date', 'image_display', 'user' ]
    list_filter = [ 'negotiable', 'created_at' ]
    actions = [ 'make_negotiable_as_false', 'make_negotiable_as_true' ]

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image', 'user'),
        }),
        ('Финансы', {
            'fields': ('price', 'negotiable'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_negotiable_as_false(self, request, queryset):
        queryset.update(negotiable=False)

    @admin.action(description='Добавить возможность торга')
    def make_negotiable_as_true(self, request, queryset):
        queryset.update(negotiable=True)

admin.site.register(Advertisement, AdvertisementAdmin)