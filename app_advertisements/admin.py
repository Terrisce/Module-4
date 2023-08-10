from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date','updated_date', 'negotiable']  
    list_filter = ['negotiable', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description'),
            'classes':['collapse']
        }),
        ('Финансы',{
            'fields':('price', 'negotiable'),
            'classes':['collapse']
        }) 
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(negotiable=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(negotiable=True)


admin.site.register(Advertisement, AdvertisementAdmin)