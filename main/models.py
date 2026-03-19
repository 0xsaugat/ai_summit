from django.db import models


class SiteContent(models.Model):
	title = models.CharField(max_length=200)
	tagline = models.CharField(max_length=255)
	event_date = models.CharField(max_length=120)
	venue = models.CharField(max_length=255)
	tickets_label = models.CharField(max_length=100, default="Tickets")
	tickets_url = models.URLField(blank=True)
	schedule_url = models.URLField(blank=True)
	community_url = models.URLField(blank=True)
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Site Content"
		verbose_name_plural = "Site Content"

	def __str__(self):
		return self.title


class NavLink(models.Model):
	label = models.CharField(max_length=80)
	url = models.URLField()
	order = models.PositiveIntegerField(default=0)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ["order", "id"]

	def __str__(self):
		return self.label


class Speaker(models.Model):
	name = models.CharField(max_length=120)
	title = models.CharField(max_length=150)
	topic = models.CharField(max_length=255)
	image_url = models.URLField(blank=True)
	order = models.PositiveIntegerField(default=0)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ["order", "id"]

	def __str__(self):
		return self.name
