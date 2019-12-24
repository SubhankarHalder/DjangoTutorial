from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL pattens
import uuid # Required for unique book instances

# Create your models here.

class Genre(models.Model):
    """ Model representing a book genre """
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        """ String for representing the Model object """
        return self.name


class Language(models.Model):
    """ Model representing a Language (e.g. English, French) """
    name = models.CharField(max_length=200, help_text="Enter the book's language")

    def __str__(self):
        """ String for representing the Model object """
        return self.name

class Book(models.Model):
    """ Model representing a book """
    title = models.CharField(max_length=200)
    # Author as a string rather than object as it hasn't been declared yet
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN')

    # Genre can contain many books and books can cover many genres. We use ManytoManyField
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)



    def __str__(self):
        """ String for representing the Model object """
        return self.title

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this book """
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """ Model representing a specific copu of a book """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """ String for representing the Model object """
        return f'{self.id}({self.book.title})'

class Author(models.Model):
    """ Model representing an author """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """ String for representing the Model object """
        return f'{self.last_name},{self.first_name}'

