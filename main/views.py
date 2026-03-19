from django.shortcuts import render

from .models import NavLink, SiteContent, Speaker


def landing_page(request):
	site = SiteContent.objects.filter(active=True).order_by("-id").first()

	if site is None:
		site = {
			"title": "AI Conf 2026",
			"tagline": "Nepal's premier conference for people building the future with AI",
			"event_date": "Jan 10-11, 2026",
			"venue": "The Plaza, Kathmandu, Nepal",
			"tickets_label": "Tickets Sold Out",
			"tickets_url": "#",
			"schedule_url": "#",
			"community_url": "https://community.wwktm.com",
		}

	nav_links = NavLink.objects.filter(is_active=True)
	speakers = Speaker.objects.filter(is_active=True)

	context = {
		"site": site,
		"nav_links": nav_links,
		"speakers": speakers,
	}
	return render(request, "landing.html", context)
