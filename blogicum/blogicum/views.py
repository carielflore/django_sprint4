from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def permission_denied(request, expection):
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    return render(request, 'pages/500.html', status=500)
