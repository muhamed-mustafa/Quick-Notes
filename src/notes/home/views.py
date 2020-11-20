from django.shortcuts import render
from notes_app.models import Note
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
# Create your views here.

def allnotes(request):
    notes = Note.objects.filter(active=True)
    paginator = Paginator(notes,3)
    page = request.GET.get('page')
    try :
        notes = paginator.get_page(page)
    except PageNotAnInteger :
        notes = paginator.get_page(1)
    except EmptyPage :
        notes = paginator.get_page(paginator.num_pages)
    context = {'notes':notes}
    return render(request,'home.html',context)