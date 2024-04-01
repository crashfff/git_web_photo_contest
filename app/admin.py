from django.contrib import admin
from .models import *

admin.site.register(Photo)
admin.site.register(CustomUser)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)



