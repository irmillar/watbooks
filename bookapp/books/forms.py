from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta():
        model = Book
        fields = ('book_title', 'author', 'publication_date', 'isbn', 'cost', 
                'genre', 'book_type')
        
        


