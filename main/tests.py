from django.test import TestCase
from django.urls import reverse

from .models import NavLink, SiteContent, Speaker


class LandingPageTests(TestCase):
	def test_landing_page_loads(self):
		response = self.client.get(reverse("main:landing"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "landing.html")

	def test_landing_page_uses_database_content(self):
		SiteContent.objects.create(
			title="Dynamic Event",
			tagline="Dynamic tagline",
			event_date="Jan 1, 2027",
			venue="Kathmandu",
			tickets_label="Buy Now",
			tickets_url="https://example.com/tickets",
			schedule_url="https://example.com/schedule",
			community_url="https://example.com/community",
			active=True,
		)
		NavLink.objects.create(label="Home", url="https://example.com", order=1, is_active=True)
		Speaker.objects.create(
			name="Jane Doe",
			title="AI Engineer",
			topic="Practical AI",
			order=1,
			is_active=True,
		)

		response = self.client.get(reverse("main:landing"))

		self.assertContains(response, "Dynamic Event")
		self.assertContains(response, "Home")
		self.assertContains(response, "Jane Doe")
