from typing import List
from django.shortcuts import render, redirect, HttpResponse
from main.models import Post, Comment
from main.services import PostService, CommentService
from main.forms import CommentForm


def post_list_view(request: HttpResponse) -> HttpResponse:
    service = PostService()
    posts: List[Post] = service.get_objects()

    context = {
        'posts': posts,
    }

    return render(request, 'main/post_list.html', context)

def post_detail_view(request: HttpResponse, id: int) -> HttpResponse:
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    comment_service = CommentService()
    comments: List[Comment] = comment_service.filter_objects(post=id).order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_service.create_object(
                post=post,
                comment=form.cleaned_data['comment'],
                author=request.user
            )
    else:
        form = CommentForm()


    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'main/post_detail.html', context)


def like_add_view(request: HttpResponse, id: int) -> HttpResponse:
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    is_like: bool = False

    for like in post.likes.all():
        if like == request.user:
            is_like = True
            break
    
    if not is_like:
        post.likes.add(request.user)

    if is_like:
        post.likes.remove(request.user)

    return redirect(f'/post/{post.id}/')
