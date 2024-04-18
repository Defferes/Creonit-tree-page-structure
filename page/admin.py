from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .forms import PageCreateForm
from .models import Page


class PageAdmin(MPTTModelAdmin):
    form = PageCreateForm
    list_display = ('name', 'slug', 'url', 'parent')


admin.site.register(Page, PageAdmin)
