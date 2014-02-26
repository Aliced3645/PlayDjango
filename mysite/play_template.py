#play python's template library

from django import template;


t = template.Template('My name is {{name}}');
c = template.Context({'name' : 'Shu Zhang'});
print t.render(c);

c = template.Context({'name' : 'Michael'})
print t.render(c);