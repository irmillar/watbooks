from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    GENRE_LIST = [
        ('FA', 'Fantasy'),
        ('SF', 'Science Fiction'),
        ('TH', 'Thriller'),
        ('MY', 'Mystery'),
        ('DY', 'Dystopia'),
        ('SS', 'Short Story'),
        ('SU', 'Surrealism'),
        ('SC', 'Science'),
        ('EC', 'Economics'),
        ('MA', 'Maths'),
        ('HI', 'History'),
        ('PH', 'Philosophy'),
        ('FI', 'Finance'),
        ('OT', 'Other'),
        ]

    BOOK_TYPES = [
        ('FI', "Fiction"),
        ('NF', "Non-Fiction"),
    ]
    

    book_title = models.CharField("Book Title", max_length = 200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField("Publication Date", null=True, blank=True)
    isbn = models.PositiveIntegerField("ISBN", null=True, blank=True, unique=True)
    cost = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)
    # Make the added date one which grabs the current date
    added_date = models.DateField(null=True, blank=True)
    borrowed_to = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=20, choices=GENRE_LIST)
    book_type = models.CharField("Fiction or Non-Fiction", max_length=40, choices=BOOK_TYPES)

    def get_absolute_url(self):
        return reverse('book_app:book_details', kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.book_title}, {self.author}"
