from django import forms

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     negotiable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

from django.core.exceptions import ValidationError
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control lg'
        self.fields['negotiable'].widget.attrs['class'] = 'form-check-input'

class Meta:
    model = Advertisement
    fields = ("title", "description", "image", "price", "negotiable")

def clean_title(self):
    title = self.cleaned_data['title']
    if title.startswith('?'):
        raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
    return title