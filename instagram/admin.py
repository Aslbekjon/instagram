from django.contrib import admin
from .models import Comment, Post, Stream, Tag
# Register your models here.

admin.site.register([Comment,Post, Stream, Tag])
