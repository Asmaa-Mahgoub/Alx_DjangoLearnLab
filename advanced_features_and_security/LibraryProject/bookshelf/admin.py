from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser   # tell Django which model to use

    # Fields shown when you open user details in Admin
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields shown when adding a NEW user in Admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_picture', 'is_staff', 'is_active')}
        ),
    )

    # Which fields to display in the user list page
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')

    # Filters on the right-hand side
    list_filter = ('is_staff', 'is_active', 'date_of_birth')

    # Search bar fields
    search_fields = ('email', 'username')

    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

