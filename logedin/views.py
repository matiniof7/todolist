from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from.form import CreateTodoForm,UpdateTodoForm



def logedin_home(request):
    todos=Todo.objects.filter(owner=request.user)
    return render(request, 'logedin/logined.html',{
        "user": request.user,
        'todos': todos
        })  


def create_todo(request):
    if request.method=='POST':
        form=CreateTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)  # don't save yet

            todo.owner = request.user        # set model field manually
            todo.save()   
        
            return redirect('Homepage')

    else:
        form=CreateTodoForm()
        
    return render(request,'logedin/create.html',{
            'form':form,
        })



def details(request , todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request,'logedin/details.html',{
        'todo':todo
    })



def delete(request , todo_id):
    get_object_or_404(Todo,id=todo_id).delete()
    return redirect('Homepage')



def update(request, todo_id):
    todo=get_object_or_404(Todo,id=todo_id)
    if request.method=='POST':
        form=UpdateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()  
             
        
            return redirect('Homepage')

    else:
        form=UpdateTodoForm(instance=todo)
        
    return render(request,'logedin/update.html',{
            'form':form,
        })




