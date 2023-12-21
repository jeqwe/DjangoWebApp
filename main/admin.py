from django.contrib import admin
from main.models import News


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def get_changeform_initial_data(self, request):
        return {
            'moderated': True,
        }


admin.site.register(News, NewsAdmin)
