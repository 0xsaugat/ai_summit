from django.test import TestCase
from django.urls import reverse

from .models import Application


class LandingPageTests(TestCase):
	def test_landing_page_loads(self):
		response = self.client.get(reverse("main:landing"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "landing.html")


class ApplyPageTests(TestCase):
	def test_apply_page_loads(self):
		response = self.client.get(reverse("main:apply"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "apply.html")

	def test_apply_page_creates_application(self):
		response = self.client.post(
			reverse("main:apply"),
			{
				"full_name": "Test Founder",
				"email": "founder@example.com",
				"role": "founder",
				"message": "Building AI tools for local businesses.",
			},
		)

		self.assertEqual(response.status_code, 302)
		self.assertTrue(response.url.startswith(reverse("main:apply")))
		self.assertEqual(Application.objects.count(), 1)
		application = Application.objects.first()
		self.assertEqual(application.full_name, "Test Founder")
		self.assertEqual(application.role, "founder")
