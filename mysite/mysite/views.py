from django.http import HttpResponse;
from django.http import HttpRequest, Http404;
import sys;
import datetime;
from django.template import Context, Template;
from django.template.loader import get_template;
from django.shortcuts import render;
#This is a view function
def hello(request):
    return HttpResponse("Hello");

def welcome(requeset):
    return HttpResponse('Welcome!');

#Second view, dynamic content
def current_datetime(request):
    now = datetime.datetime.now();
    
    #html = "<html><body>It is now %s </body></html>" %now;
    #return HttpResponse(html);
    
    #t = Template('<html><body>It is now {{time}} </body></html>');
    #c = Context({'time' : now});
    #return HttpResponse(t.render(c));

    #We are reading template from file system
    #t = get_template('current_datetime.html');
    #c = Context({'time' : now});
    #return HttpResponse(t.render(c));
    
    #one liner
    return render(request, 'current_datetime.html', {'time':now});

#Third view, with wildcard url patterns.
def hours_ahead(request, offset):
    try:
        offset = int(offset);
    except ValueError:
        raise Http404();
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset);
    html = '<html><body>In %s hour(s), it will be %s.</body></html>' %(offset, dt)
    return HttpResponse(html);



