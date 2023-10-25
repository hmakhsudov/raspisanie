from django.contrib import admin
from .models import Pair  # Import your Pair model from your app

class PairAdmin(admin.ModelAdmin):
    list_display = ('sbj', 'teacher', 'day', 'lesson_index', 'group', 'seat_number')  # Customize the list display fields
    list_filter = ('group',)  # Add 'group' to the list of fields for filtering

# Register the Pair model with the custom admin class
admin.site.register(Pair, PairAdmin)
