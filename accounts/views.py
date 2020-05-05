from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import News
from order.models import orderForm

def home(request):
    new = News.objects
    return render(request, 'accounts/home.html', {"news":new})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error':'Email Address Already exists'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'], email=request.POST['email'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
    else:        
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password does not match'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required
def account(request):
    User = request.user
    orders = orderForm.objects.all()
    if User.username == 'admin':
        return render(request, 'accounts/adminaccount.html', {'order':orders})
    else:
        return render(request, 'accounts/account.html')

@login_required
def updatestatus(request, orderForm_id):
    if request.method == 'POST':
        updateorder = get_object_or_404(orderForm, pk=orderForm_id)
        updateorder.status = request.POST['status']
        updateorder.save()
        return render(request, 'accounts/adminaccount.html')
