from django.contrib import admin
from .models import Video, Subtitle

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', )
    search_fields = ('title',)
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)
    readonly_fields = ('uploaded_at',)

@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ('video', 'language',) 
    search_fields = ('video__title', 'language')
    list_filter = ('language',)
    ordering = ('video', 'language')
    readonly_fields = ('video',)
    fieldsets = (
        (None, {
            'fields': ('video', 'language', 'content')
        }),
    )
