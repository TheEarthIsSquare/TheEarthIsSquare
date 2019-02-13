from django.forms import ModelForm
from django import forms

class ContactForm_Coffee(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Who are you?','class' : '-field'})
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'What\'s your email?', 'class' : '-field'})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'What do you want to talk about?','class' : '-field'})
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'What city are you in?','class' : '-field'})
    )

class ContactForm_Work(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Who are you?','class' : '-field'})
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'What\'s your email?', 'class' : '-field'})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'What do you want to talk about?','class' : '-field'})
    )
    type = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'What type of work are you after?','class' : '-field'})
    )

class ContactForm_Other(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Who are you?','class' : '-field'})
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'What\'s your email?', 'class' : '-field'})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'What do you want to talk about?','class' : '-field'})
    )
