from django import forms 
from .models import userData, bookData

class userDataForm(forms.ModelForm):
    address = forms.CharField(required=False)
    class Meta:
        model = userData
        fields = ['full_name', 'email', 'phone_no', 'address', 'status']

class bookDataForm(forms.ModelForm):
    class Meta:
        model = bookData
        fields = ['book_name', 'author', 'types', 'stock', 'status']