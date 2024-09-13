
from .models import FlightPassenger
from django import forms

class FlightPassengerForm(forms.ModelForm):
    class Meta:
        model = FlightPassenger
        fields = ['full_name','gender','date_of_birth','nationality','phone_number','email_address','box_number','emmergency_phone_number','passport_number','visa_document','departure_city','destination_city']

        labels = {
            'full_name':'Full Name',
            'gender':'Gender',
            'date_of_birth': 'Date Of Birth',
            'nationality': 'Nationality',
            'phone_number':'Phone Number',
            'email_address':'Email Address',
            'box_number': 'P.O Box Number',
            'emmergency_phone_number': 'Emmergency Phone Number',
            'passport_number': 'Passport Number',
            'visa_document': 'Visa Document',
            'departure_city': 'Departure City',
            'destination_city': 'Destination City'
        }

        widgets = {
            'full_name':forms.TextInput(attrs={}),
            'gender':forms.Select(choices=FlightPassenger.GENDER),
            'date_of_birth':forms.DateInput(attrs={'placeholder':'YYYY/MM/DD', 'type':'date'}),
            'nationality':forms.TextInput(attrs={'placeholder':''}),
            'phone_number':forms.NumberInput(attrs={}),
            'email_address':forms.EmailInput(attrs={}),
            'box_number':forms.TextInput(attrs={}),
            'emmergency_phone_number':forms.NumberInput(attrs={}),
            'passport_number':forms.NumberInput(attrs={}),
            'visa_document':forms.FileInput(attrs={}),
            'departure_city':forms.TextInput(attrs={}),
            'destination_city':forms.TextInput(attrs={})

        }