from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from user.services import UserService
from main.services import PostService
from user.models import User
from main.models import Post


@login_required
def dashboard_view(request: HttpResponse) -> HttpResponse:
    return render(request, 'dashboard/dashboard_base.html')

@login_required
def account_list_view(request: HttpResponse) -> HttpResponse:
    user_service = UserService()
    accounts: User = user_service.get_objects()

    context = {
        'accounts': accounts,
    }

    return render(request, 'dashboard/accounts.html', context)

@login_required
def account_posts_view(request: HttpResponse, id: int) -> HttpResponse:
    user_service = UserService()
    account: User = user_service.get_object_by_id(id)

    post_service = PostService()
    posts: Post = post_service.filter_objects(id)

    context = {
        'account': account,
        'posts': posts,
    }

    return render(request, 'dashboard/account.html', context)
