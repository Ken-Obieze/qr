from django import forms


class QRCodeForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name your Document'
            })
        )
    url = forms.URLField(
        label='URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL for QR code'
            })
        )
