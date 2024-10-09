from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        # if len(message.split()) < 10:
        #     raise forms.ValidationError('پیام باید حداقل شامل ۱۰ کلمه باشد.')
        return message
