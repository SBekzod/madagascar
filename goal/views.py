from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .utils import dict_fetchall


def home_view(request, *args, **kwargs):
    select_goals_sql = render_to_string('sql/select_goals.sql')
    select_goals = dict_fetchall(select_goals_sql)
    return render(request, "pages/home.html", {'goals': select_goals}, status=200)

