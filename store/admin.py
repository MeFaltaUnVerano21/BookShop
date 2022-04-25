from django.contrib import admin
from .models import  Book, Slider




class AddBook(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['price', 'stock', 'status']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, AddBook)

class AddSlider(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
	#list_editable = ['title',]

admin.site.register(Slider, AddSlider) 