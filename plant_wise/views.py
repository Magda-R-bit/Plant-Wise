from django.shortcuts import render


def handler404(request, exception):
    """ Custom 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Custom 500 - Page Not Found
    """
    return render(request, "errors/500.html", status=500)
