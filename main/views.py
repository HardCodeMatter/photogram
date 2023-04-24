from typing import List
from django.shortcuts import render, HttpResponse
from main.models import Post
from main.services import PostService


def post_list_view(request: HttpResponse) -> HttpResponse:
    service = PostService()
    posts: List[Post] = service.get_objects()

    context = {
        'posts': posts,
    }

    return render(request, 'main/post_list.html', context)
