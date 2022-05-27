from django import forms

class ContactForms(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'})
    )
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'})
    )
    phone = forms.CharField(
        label="phone",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone'})
    )
    message = forms.CharField(
        label="message",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Message'})
    )