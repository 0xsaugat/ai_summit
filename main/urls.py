from django.urls import path

from .views import (
    about_page,
    ai_summit_page,
    apply_page,
    community_page,
    events_page,
    gallery_page,
    landing_page,
    programs_page,
    team_page,
)

app_name = "main"

urlpatterns = [
    path("", landing_page, name="landing"),
    path("about/", about_page, name="about"),
    path("programs/", programs_page, name="programs"),
    path("events/", events_page, name="events"),
    path("ai-summit/", ai_summit_page, name="ai_summit"),
    path("gallery/", gallery_page, name="gallery"),
    path("team/", team_page, name="team"),
    path("community/", community_page, name="community"),
    path("apply/", apply_page, name="apply"),
]
