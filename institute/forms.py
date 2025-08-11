from django import forms
from institute import models


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = models.GetInTouch
        fields =["name","email","phone", "message"]


class DemoClassForm(forms.ModelForm):
    class Meta:
        model = models.DemoClassBooking
        fields = '__all__'


class TutorRegForm(forms.ModelForm):
    class Meta:
        model = models.TutorRegistrations
        fields = '__all__'