import json 
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .utils import dict_fetchall


def home_view(request, *args, **kwargs):
    print('home_view')
    
    select_goals_sql = render_to_string('sql/select_goals.sql')
    select_goals = dict_fetchall(select_goals_sql)
    return render(request, "pages/home.html", {'goals': select_goals}, status=200)


@csrf_exempt
def create_goal_view(request, *args, **kwargs):
    print('create_goal_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        create_goal = render_to_string('sql/create_goal.sql', {'goalContent': data['goalContent']})
        dict_fetchall(create_goal)  
        
        last_insert_id_sql = "SELECT LAST_INSERT_ID() as goalId;"
        last_insert_id = dict_fetchall(last_insert_id_sql)[0]
        
        print('Created Goal:', {data['goalContent'], last_insert_id['goalId']})
        return JsonResponse({'status': 'success', 'goalId': last_insert_id['goalId']})
    

@csrf_exempt
def update_goal_view(request, *args, **kwargs):
    print('update_goal_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        goalContent = data.get('new_goal')
        goal_id = data.get('id')
        
        update_goal = render_to_string('sql/update_goal.sql', {'goalContent': goalContent, 'goalId': goal_id})
        dict_fetchall(update_goal)
        
        print("Updated Goal:", {'goalContent': goalContent, 'goalID': goal_id}) 
        return JsonResponse({'status': 'success'})
    
    
@csrf_exempt
def delete_goal_view(request, *args, **kwargs):
    print('delete_goal_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        goal_id = data.get('id')

        delete_single_goal = render_to_string('sql/delete_single_goal.sql', {'goalId': goal_id})
        dict_fetchall(delete_single_goal)  
        return JsonResponse({'status': 'success'})
    

@csrf_exempt
def delete_all_goals_view(request):
    print('delete_all_goals_view')
    
    if request.method == 'POST':
        delete_all_goals_sql = render_to_string('sql/delete_all_goals.sql')
        dict_fetchall(delete_all_goals_sql)
        return JsonResponse({'status': 'success'})