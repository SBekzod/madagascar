import json 
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .utils import dict_fetchall


def home_view(request, *args, **kwargs):
    select_goals_sql = render_to_string('sql/select_goals.sql')
    select_goals = dict_fetchall(select_goals_sql)
    return render(request, "pages/home.html", {'goals': select_goals}, status=200)


@csrf_exempt
def create_goal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        create_goal = render_to_string('sql/create_goal.sql', {'goalContent': data['goalContent']})
        dict_fetchall(create_goal)  
        return JsonResponse({'status': 'success'})