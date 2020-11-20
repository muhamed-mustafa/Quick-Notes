from django.shortcuts import get_object_or_404, redirect, render
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
# Create your views here.

# This Function Show All Notes
def all_notes(request):
    all_notes = Note.objects.filter(user=request.user)
    paginator = Paginator(all_notes,3)
    page = request.GET.get('page')
    try :
        all_notes = paginator.get_page(page)
    except PageNotAnInteger :
        all_notes = paginator.get_page(1)
    except EmptyPage :
        all_notes = paginator.get_page(paginator.num_pages)
    context = {'all_notes':all_notes}
    return render(request,'notes.html',context)

# This Function Show One Note by slug
def one_note(request,slug):
    one_note = Note.objects.get(slug=slug)
    context = {'one_note':one_note}
    return render(request,'one_note.html',context)

# This Function Add New Note 
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request,'Succesfully.. Your Note Is Created ')
            return redirect('notes:all_notes')
    else:
        form = NoteForm()

    context = {'form':form}

    return render(request,'add_note.html',context)

# This Function Edit Note 
def edit_note(request,slug):
    note = get_object_or_404(Note,slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request,'Succesfully.. Your Note Is Updated ')
            return redirect('notes:one_note',slug=slug)
    else:
        form = NoteForm(instance=note)

    context = {'form':form}

    return render(request,'edit_note.html',context)
