from django.shortcuts import render, redirect


def error404(request):
    context = {
        "title": "Error 404"
    }
    return render(request, "error404.html", context)


def error403(request):
    context = {
        "title": "Error 403"
    }
    return render(request, "error403.html", context)


def error500(request):
    context = {
        "title": "Error 500"
    }
    return render(request, "error500.html", context)
