from django.contrib import admin
from core.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)