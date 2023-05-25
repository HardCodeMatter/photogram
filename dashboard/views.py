from django.shortcuts import render, HttpResponse


def dashboard_view(request: HttpResponse) -> HttpResponse:
    return render(request, 'dashboard/dashboard_base.html')
