from django.contrib import admin
from .models import *


admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BookInstance)