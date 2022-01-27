from django.contrib import admin
from .models import Profile,Following
from django.utils.safestring import mark_safe
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'get_pthoto')
    list_display_links = ('id','username')
    search_fields = ('username', )

    def get_pthoto(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" style="height:100px;width:100px">')
        else:
            return "Rasm joylanmagan"
    get_pthoto.short_description = "Rasmi"

admin.site.register(Profile)
admin.site.register(Following)