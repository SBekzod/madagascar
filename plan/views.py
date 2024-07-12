import json 
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .utils import dict_fetchall


def home_view(request, *args, **kwargs):
    print('home_view')
    
    select_plans_sql = render_to_string('sql/select_plans.sql')
    select_plans = dict_fetchall(select_plans_sql)
    return render(request, "pages/home.html", {'plans': select_plans}, status=200)


@csrf_exempt
def create_plan_view(request, *args, **kwargs):
    print('create_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        create_plan = render_to_string('sql/create_plan.sql', {'content': data['content']})
        dict_fetchall(create_plan)  
        
        last_insert_id_sql = "SELECT LAST_INSERT_ID() as id;"
        last_insert_id = dict_fetchall(last_insert_id_sql)[0]
        
        print('Created Plan:', {'content': data['content'], 'id': last_insert_id['id']})
        return JsonResponse({'status': 'success', 'id': last_insert_id['id']})
    

@csrf_exempt
def update_plan_view(request, *args, **kwargs):
    print('update_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('new_plan')
        id = data.get('id')
        
        update_plan = render_to_string('sql/update_plan.sql', {'content': content, 'id': id})
        dict_fetchall(update_plan)
        
        print("Updated Plan:", {'content': content, 'id': id}) 
        return JsonResponse({'status': 'success'})
    
    
@csrf_exempt
def delete_plan_view(request, *args, **kwargs):
    print('delete_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')

        delete_single_plan = render_to_string('sql/delete_single_plan.sql', {'id': id})
        dict_fetchall(delete_single_plan)  
        return JsonResponse({'status': 'success'})
    

@csrf_exempt
def delete_all_plans_view(request):
    print('delete_all_plans_view')
    
    if request.method == 'POST':
        delete_all_plans_sql = render_to_string('sql/delete_all_plans.sql')
        dict_fetchall(delete_all_plans_sql)
        return JsonResponse({'status': 'success'})