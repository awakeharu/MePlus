from django import forms
from shop.models import Post_Sale, Post_Sale_Comment

class PostSaleForm(forms.ModelForm):
    class Meta:
        model = Post_Sale
        fields = ['title','content','image']
        
class SaleCommentForm(forms.ModelForm):
    class Meta:
        model = Post_Sale_Comment
        fields = ['message']