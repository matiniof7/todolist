from django.shortcuts import render, redirect
from .forms import registerform, loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):  
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)  # call Django's login
                return redirect('Homepage')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = loginform()
    
    return render(request, 'accounts/login.html', {'form': form})

def register(request):


    if request.method=='POST':

        form=registerform(request.POST)
        
        if form.is_valid():
                cd=form.cleaned_data
                User.objects.create_user(cd['username'],cd['gmail'],cd['password'])
                
                return redirect('Homepage')



        return render(request,'accounts/register.html',{
            'form':form
            })
   
    else:
        form=registerform

    return render(request,'accounts/register.html',{
            'form':form
        })
    


    