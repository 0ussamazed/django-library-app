from django import forms
from .models import Book, Category
from django.utils import timezone

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }






class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.created_at:
            self.fields['created_at'].initial = self.instance.created_at.strftime('%Y-%m-%dT%H:%M')
        else:
            now = timezone.now()
            self.fields['created_at'].initial = now.strftime('%Y-%m-%dT%H:%M')
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_image',
            'author_image',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'total_rental',
            'status',
            'category',
            'created_at',
            'client_name',
            'client_phone',
            'client_address',
            
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'book_image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'author_image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'retal_price_day' : forms.NumberInput(attrs={'class' : 'form-control retal__PriceDay', 'id' : 'retalPriceDay'}),
            'retal_period' : forms.NumberInput(attrs={'class' : 'form-control retal__Period', 'id' : 'retalPeriod'}),
            'total_rental' : forms.NumberInput(attrs={'class' : 'form-control total__Rental', 'id' : 'totalRental', 'readonly': 'readonly'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),
            'isActive' : forms.CheckboxInput(attrs={'class' : 'form-control col-1'}),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'type': 'datetime-local'
            }),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'clientName'}),
            'client_phone': forms.NumberInput(attrs={'class': 'form-control', 'id': 'clientPhone'}),
            'client_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'id': 'clientAddress'}),

            
        }