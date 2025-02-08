from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(max_length=300, widget=forms.Textarea, label='Message')