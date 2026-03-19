from django.contrib import admin

from .models import NavLink, SiteContent, Speaker


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
	list_display = ("title", "event_date", "venue", "active")
	list_filter = ("active",)
	search_fields = ("title", "tagline", "venue")


@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
	list_display = ("label", "url", "order", "is_active")
	list_filter = ("is_active",)
	search_fields = ("label", "url")
	ordering = ("order",)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
	list_display = ("name", "title", "topic", "order", "is_active")
	list_filter = ("is_active",)
	search_fields = ("name", "title", "topic")
	ordering = ("order",)
