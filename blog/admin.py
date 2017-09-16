from django.contrib import admin

# Register your modelspython manage.py migrate blogfrom .models import Post

from .models import Post

admin.site.register(Post)
