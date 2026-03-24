from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ApplicationForm, TicketBookingForm


def landing_page(request):
	if request.method == "POST":
		form = TicketBookingForm(request.POST)
		if form.is_valid():
			booking = form.save()
			return HttpResponseRedirect(f"{reverse('main:landing')}?booked=1&ref={booking.booking_reference}#tickets")
	else:
		form = TicketBookingForm(initial={"pass_type": "pro", "quantity": 1})

	context = {
		"ticket_form": form,
		"booking_success": request.GET.get("booked") == "1",
		"booking_reference": request.GET.get("ref", ""),
	}
	return render(request, "landing.html", context)


def about_page(request):
	return render(request, "about.html")


def programs_page(request):
	return render(request, "programs.html")


def events_page(request):
	return render(request, "events.html")


def ai_summit_page(request):
	return render(request, "ai_summit.html")


def gallery_page(request):
	return render(request, "gallery.html")


def team_page(request):
	return HttpResponseRedirect(f"{reverse('main:about')}#team-section")


def community_page(request):
	return HttpResponseRedirect(f"{reverse('main:about')}#community-section")


def apply_page(request):
	if request.method == "POST":
		form = ApplicationForm(request.POST)
		if form.is_valid():
			application = form.save()
			return HttpResponseRedirect(
				f"{reverse('main:apply')}?submitted=1&ref={application.application_reference}"
			)
	else:
		form = ApplicationForm(initial={"role": "founder"})

	context = {
		"application_form": form,
		"application_success": request.GET.get("submitted") == "1",
		"application_reference": request.GET.get("ref", ""),
	}
	return render(request, "apply.html", context)
