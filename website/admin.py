from django.contrib import admin

from .models import ContactMessage, Project, Service, SiteSettings


admin.site.site_header = "Taşcan Mühendislik Yönetim Paneli"
admin.site.site_title = "Taşcan Mühendislik Admin"
admin.site.index_title = "İçerik ve mesaj yönetimi"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Marka", {"fields": ("company_name", "tagline", "about_text")} ),
        ("İletişim", {"fields": ("phone", "email", "address")} ),
    )
    list_display = ("company_name", "phone", "email", "updated_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short_description", "description")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "year", "is_featured", "order")
    list_editable = ("is_featured", "order")
    list_filter = ("category", "year", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "category", "location", "summary")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "created_at", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
