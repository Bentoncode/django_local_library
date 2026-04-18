from django.contrib import admin

from .models import Author, Book, Genre, BookInstance, Language 


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookinlineAdmin(admin.StackedInline):
    # Define book inline under author
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # changing fields display to horizontal of vertical, the fault is Vertical.
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # Inlines list for author 
    inlines = [BookinlineAdmin]
   
    

# Register the Admin class with the associtated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the Admin classes for Book using decorator
@admin.register(Book)  
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # Bookinstance inlines for books
    inlines = [BooksInstanceInline]



# Register the Admin classes for Book using decorator.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'due_back', 'id' ]
    list_filter = ('status', 'due_back')
    # Arranging fields as vertical or horizontal and labeling.
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

