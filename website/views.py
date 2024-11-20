from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer

def home(request):
    customers = Customer.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        
        messages.error(request, "There Was An Error Logging in, Please Try Again...")
        return redirect('home')
            
    return render(request, 'home.html', {'customers' : customers})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})
    
    return render(request, "register.html", {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer':customer})
    messages.error(request, "You must be logged in to see customers detail")
    return redirect('home')