from django.contrib import admin
from techblog.blog.models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)
