from django.db import models
from django import forms


class Reservation(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.subject


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['subject', 'message', 'name', 'email']
