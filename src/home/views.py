from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from home.models import Task
from home.forms import TaskForm


# Create your views here.

def Home(request):

    form = TaskForm()
    remaining_tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    context = {
        'form': form,
        'remaining_tasks': remaining_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home/home.html', context)


def addTask(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Task Added succesfully'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
        
    return JsonResponse({'error': 'Invalid Request'}, status=400)



def editTask(request, task_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('ajax call received')
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            print('form valid and saved')
            return JsonResponse({'message': 'Task successfuly updated'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
        
    else:
        return JsonResponse({'error': 'Invalid Request'}, status=400)
    
@require_POST
def deleteTask(request, task_id):
    
    
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'Success':'Task successfully deleted'})


@csrf_exempt
def updateTaskStatus(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        completed = request.POST.get('completed') == 'True'

        task = Task.objects.get(id=task_id)
        task.completed = completed
        task.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})