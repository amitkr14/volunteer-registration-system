from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class VolunteerSignUpForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_volunteer = True 
        
        if commit:
            user.save()
        return user