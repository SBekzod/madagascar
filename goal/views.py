from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect, render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)
