from django.shortcuts import render
from django.http import HttpResponse;
from django.http import HttpRequest;
from models import Book;
from forms import ContactForm;
from django.http import HttpResponseRedirect;
from django.core.mail import send_mail;

# Create your views here.
def search_form(request):
    return render(request, "search_form.html");

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q'];
        books = Book.objects.filter(title__icontains=q);
        return render(request, 'search_results.html',
                       {'books': books, 'query' : q});
    else:
        return render(request, 'search_form.html', {'error': True});
    
    
def onesearch(request):
    error = False;
    length = False;
    if 'q' in request.GET:
        q = request.GET['q'];
        if not q:
            error = True;
        elif len(q) > 20:
            error = True;
        else:
            books = Book.objects.filter(title__icontains=q);
            return render(request, 'search_results.html',
                       {'books': books, 'query' : q});
    return render(request, 'search_form.html', {'error' : error});

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})