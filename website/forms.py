from django.forms import ModelForm
from django import forms

class ContactForm(forms.Form):
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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
