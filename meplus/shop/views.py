from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect , render, get_object_or_404
from shop.models import Post_Sale, Post_Sale_Comment
from shop.forms import PostSaleForm, SaleCommentForm


# Create your views here.
def post_sale_list(request):
    return render(request, 'shop/index.html',{
        'post': Post_Sale.objects.last(),
    })

def post_sale_new(request):
    if request.method == 'POST':
        form = PostSaleForm(request.POST, request.FILES)
        if form.is_valid():
            #검증이 끝난 값
            post = form.save(commit=False)
            post.save()
            messages.success(request, '새 포스팅을 작성했습니다.')
            return redirect('shop:post_sale_detail', post.pk)
    else:
        form = PostSaleForm()
    return render(request , 'shop/post_form.html',{
            'form' : form,
        })


def post_sale_detail(request, pk):
    post = Post_Sale.objects.get(pk=pk)
    comments = post.comment_set.all()

    #GET 요청시 detail view 반환
    comment_form = SaleCommentForm()

    return render(request, 'shop/post_sale_detail.html',{
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
    })