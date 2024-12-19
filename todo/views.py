from django.shortcuts import render, redirect, HttpResponse
from todo.models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    title = request.POST.get('title')
    if request.POST.get('task_id'):
        _id = request.POST.get('task_id')
        task = Task.objects.get(id=_id)
        task.title = title
        task.save()
    else:
        Task.objects.create(title=title)
    return redirect('/')


def append_task(request, pk):
    task = Task.objects.get(id=pk)
    return HttpResponse(f'''<input name="task_id" type="hidden" value='{task.id}'/>
                        
<input id="input" placeholder="Enter Todo" value='{task.title}' name="title" required />''')

def change_status(request, pk):
    print('change status')
    task = Task.objects.get(pk=pk)
    status = request.POST.get('checkbox')
    print('status=============', status)
    if status=='False':
        
        task.status=True
    else:
        task.status = False
    task.save()
    return redirect('/')


def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()
    return redirect('/')
  