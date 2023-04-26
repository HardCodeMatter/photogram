from typing import List
from django.shortcuts import render, HttpResponse
from main.models import Post, Comment
from main.services import PostService, CommentService


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
    comments: List[Comment] = comment_service.filter_objects(post=id)

    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'main/post_detail.html', context)
