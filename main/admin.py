from django.contrib import admin

from .models import Application, TicketBooking


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ("application_reference", "full_name", "email", "role", "status", "created_at")
	list_filter = ("role", "status", "created_at")
	search_fields = ("application_reference", "full_name", "email")


@admin.register(TicketBooking)
class TicketBookingAdmin(admin.ModelAdmin):
	list_display = ("booking_reference", "full_name", "email", "pass_type", "quantity", "amount_npr", "status", "created_at")
	list_filter = ("pass_type", "status", "created_at")
	search_fields = ("booking_reference", "full_name", "email", "phone")
