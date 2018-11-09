from django.db import models
#import uuid

class Language(models.Model):
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField(blank=True, null=True)
    #email = models.

    def getFullName(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.getFullName()

    class Meta:
        ordering=['first_name']


class Author(Person):
    
    born_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Student(Person):

    UNIVERSITY_YEARS = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate')
    )
    
    degree_year = models.CharField(max_length=2, choices=UNIVERSITY_YEARS)


class Book(models.Model):

    isbn = models.CharField(max_length=20, primary_key=True)    #!Find out about isbn chars
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    written_date = models.DateField(blank=True)
    summary = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    
    LOAN_STATUS = (
        ('M', 'Maintenance'),
        ('A', 'Available'),
        ('O', 'On loan'),
        ('N', 'Not available')
    )

    #id = models.UUIDField(primary_key=True, editable=False)
    title = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    date_due = models.DateField()
    borrower = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='M')

    

    

