from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from typing import List
from main.models import Post, Comment
from main.services import PostService, CommentService, ReportService
from main.forms import PostForm, CommentForm, CommentUpdateForm


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

@login_required
def post_create_view(request: HttpResponse) -> HttpResponse:
    post_service = PostService()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post: Post = post_service.create_object(
                image=form.cleaned_data['image'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                author=request.user,
            )

            return redirect(f'/post/{post.id}/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'main/post_create.html', context)

@login_required
def post_update_view(request: HttpResponse, id: int) -> HttpResponse:
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    if request.user != post.author:
        return redirect(f'/post/{id}/')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post_service.update_object(
                id,
                image=form.cleaned_data['image'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
            )

            return redirect(f'/post/{id}/update/')
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'main/post_update.html', context)

@login_required
def post_delete_view(request: HttpResponse, id: int) -> HttpResponse:
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    if request.user != post.author:
        return redirect(f'/post/{id}/')

    post_service.delete_object(id)
    
    return redirect(f'/')


@login_required
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


@login_required
def comment_update_view(request: HttpResponse, id: int) -> HttpResponse:
    comment_service = CommentService()
    comment: Comment = comment_service.get_object_by_id(id)
    
    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance=comment)

        if form.is_valid():
            comment_service.update_object(
                id,
                comment=form.cleaned_data['comment'],
                date_updated=timezone.now(),
            )

            return redirect(f'/post/{comment.post_id}/')
    else:
        form = CommentUpdateForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, 'main/comment_update.html', context)

@login_required
def comment_delete_view(request: HttpResponse, id: int) -> HttpResponse:
    comment_service = CommentService()
    comment: Comment = comment_service.get_object_by_id(id)

    if request.user != comment.author:
        return redirect(f'/post/{comment.post_id}/')

    comment_service.delete_object(id)
    
    return redirect(f'/post/{comment.post_id}/')


@login_required
def report_create_view(request: HttpResponse, id: int) -> HttpResponse:
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    report_service = ReportService()
    
    if request.method == 'POST':
        report_service.create_object(
            reason=request.POST.get('reason'),
            post=post,
            post_author=post.author,
            report_author=request.user,
        )

        return redirect(f'/post/{post.id}/')

    context = {
        'post': post,
    }

    return render(request, 'main/report_create.html', context)

@login_required
def post_status_view(request: HttpResponse, id: int) -> HttpResponse:
    """Must be in the admin panel"""
    post_service = PostService()
    post: Post = post_service.get_object_by_id(id)

    post_service.update_object(
        id,
        is_active=not post.is_active,
    )

    return redirect(f'/post/{post.id}/')
