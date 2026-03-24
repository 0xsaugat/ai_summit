from django import forms

from .models import Application, TicketBooking


class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = TicketBooking
        fields = ["full_name", "email", "phone", "pass_type", "quantity", "notes"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+977-98XXXXXXXX"}),
            "notes": forms.Textarea(attrs={"placeholder": "Any special request", "rows": 3}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        if quantity > 10:
            raise forms.ValidationError("Maximum 10 tickets per booking.")
        return quantity


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["full_name", "email", "role", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your profile", "rows": 4}),
        }
