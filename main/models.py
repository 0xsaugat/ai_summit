import uuid

from django.db import models


class TicketBooking(models.Model):
	STUDENT = "student"
	PRO = "pro"
	VIP = "vip"

	PASS_TYPE_CHOICES = [
		(STUDENT, "Student Pass"),
		(PRO, "Pro Pass"),
		(VIP, "VIP Pass"),
	]

	STATUS_CHOICES = [
		("pending", "Pending"),
		("confirmed", "Confirmed"),
		("cancelled", "Cancelled"),
	]

	booking_reference = models.CharField(max_length=20, unique=True, editable=False)
	full_name = models.CharField(max_length=120)
	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True)
	pass_type = models.CharField(max_length=20, choices=PASS_TYPE_CHOICES, default=PRO)
	quantity = models.PositiveIntegerField(default=1)
	notes = models.TextField(blank=True)
	amount_npr = models.PositiveIntegerField(default=0, editable=False)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.booking_reference} - {self.full_name}"

	def get_unit_price(self):
		prices = {
			self.STUDENT: 1500,
			self.PRO: 2500,
			self.VIP: 5000,
		}
		return prices.get(self.pass_type, 2500)

	def save(self, *args, **kwargs):
		if not self.booking_reference:
			while True:
				candidate = f"TSN-{uuid.uuid4().hex[:8].upper()}"
				if not TicketBooking.objects.filter(booking_reference=candidate).exists():
					self.booking_reference = candidate
					break

		self.amount_npr = self.get_unit_price() * max(self.quantity, 1)
		super().save(*args, **kwargs)


class Application(models.Model):
	FOUNDER = "founder"
	MENTOR = "mentor"
	INVESTOR = "investor"
	PARTNER = "partner"

	ROLE_CHOICES = [
		(FOUNDER, "Founder"),
		(MENTOR, "Mentor"),
		(INVESTOR, "Investor"),
		(PARTNER, "Partner"),
	]

	STATUS_CHOICES = [
		("new", "New"),
		("reviewing", "Reviewing"),
		("accepted", "Accepted"),
		("rejected", "Rejected"),
	]

	application_reference = models.CharField(max_length=20, unique=True, editable=False)
	full_name = models.CharField(max_length=120)
	email = models.EmailField()
	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=FOUNDER)
	message = models.TextField(blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.application_reference} - {self.full_name}"

	def save(self, *args, **kwargs):
		if not self.application_reference:
			while True:
				candidate = f"APP-{uuid.uuid4().hex[:8].upper()}"
				if not Application.objects.filter(application_reference=candidate).exists():
					self.application_reference = candidate
					break

		super().save(*args, **kwargs)
