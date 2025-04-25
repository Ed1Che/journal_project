from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Entry
from .forms import EntryForm

def landing_page(request):
    return render(request, 'journal/landing_page.html')

def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_entries')
    else:
        form = EntryForm()
    return render(request, 'journal/new_entry.html', {'form': form})

def review_entries(request):
    entries = Entry.objects.all().order_by('-date_created')
    return render(request, 'journal/review_entries.html', {'entries': entries})
# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'journal/login.html')

# User Signup
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'journal/signup.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('landing_page')

# Create Entry (Only for logged-in users)
from django.contrib.auth.decorators import login_required

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # Assign entry to logged-in user
            entry.save()
            return redirect('review_entries')
    else:
        form = EntryForm()
    return render(request, 'journal/new_entry.html', {'form': form})

# Review Entries (Only for logged-in users)
@login_required
def review_entries(request):
    entries = Entry.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'journal/review_entries.html', {'entries': entries})