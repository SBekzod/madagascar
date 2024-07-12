import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Plan


def home_view(request, *args, **kwargs):
    print('home_view')
    
    select_plans = Plan.objects.all()
    return render(request, "pages/home.html", {'plans': select_plans}, status=200)


@csrf_exempt
def create_plan_view(request, *args, **kwargs):
    print('create_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        new_plan = Plan.objects.create(content=data['content'])
        
        print('Created Plan:', {'content': data['content'], 'id': new_plan.id})
        return JsonResponse({'status': 'success', 'id': new_plan.id})
    

@csrf_exempt
def update_plan_view(request, *args, **kwargs):
    print('update_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('new_plan')
        plan_id = data.get('id')
        
        try:
            plan = Plan.objects.get(id=plan_id)
            plan.content = content
            plan.save()
            print("Updated Plan:", {'content': content, 'id': plan.id}) 
            return JsonResponse({'status': 'success'})
        except Plan.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Plan not found'}, status=404)
    
    
@csrf_exempt
def delete_plan_view(request, *args, **kwargs):
    print('delete_plan_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        plan_id = data.get('id')
        
        try:
            plan = Plan.objects.get(id=plan_id)
            plan.delete()
            return JsonResponse({'status': 'success'})
        except Plan.DoesNotExist:
            return JsonResponse({'status': 'fail', 'message': 'Plan not found'}, status=404)
    

@csrf_exempt
def delete_all_plans_view(request):
    print('delete_all_plans_view')
    
    if request.method == 'POST':
        Plan.objects.all().delete()
        return JsonResponse({'status': 'success'})
