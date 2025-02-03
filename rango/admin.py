from django.contrib import admin
from rango.models import Category, Page

class PageInline(admin.TabularInline):  
    model = Page
    extra = 1  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes') 
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)  
    list_filter = ('views', 'likes')  

    fieldsets = (
        ('General Info', {'fields': ('name', 'slug')}),
        ('Statistics', {'fields': ('views', 'likes')}),
    )
    inlines = [PageInline]

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'created_at') 
    search_fields = ('title', 'category__name')  
    list_filter = ('category', 'created_at') 

    fieldsets = (
        ('Page Information', {'fields': ('category', 'title', 'url')}),
        ('Meta Information', {'fields': ('views', 'created_at')}),
    )
class MyAdminSite(admin.AdminSite):
    site_header = "Django administration"
    site_title = "Django administration"
    index_title = "Welcome, Admin!"

admin.site = MyAdminSite()

class CategoryAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('admin/css/custom_admin.css',)}
        js = ('admin/js/custom_admin.js',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
