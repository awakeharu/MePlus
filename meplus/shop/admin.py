from django.contrib import admin
from django.utils.safestring import mark_safe #html tag allow
from shop.models import Post_Sale, Post_Sale_Comment
# Register your models here.


@admin.register(Post_Sale)
class PostSaleAdmin(admin.ModelAdmin):
    list_display = ['title','content_len', 'created_at','updated_at']
    list_display_links = ['title']
    search_fields = ['title']

    #admin custom 하는 방법
    def content_len(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.contents)))  
    content_len.short_description = '내용 글자수'
    #content_len.allow_tags = True 사라질예정


admin.site.register(Post_Sale_Comment)
