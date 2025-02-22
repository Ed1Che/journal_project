from django.shortcuts import render, redirect
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