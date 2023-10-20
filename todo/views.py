from django.shortcuts import render
from. forms import *
from. models import *

# Create your views here.
def index(request):
    todo_item=Todolist.objects.all()
    # form_obj=Todo_form()
    if request.method=='POST':
        if 'save' in request.POST:
            form=Todo_form(request.POST)
            form.save()
    
    context={
        # "form_obj":form_obj,
        "todo_item":todo_item
    }

    
    

    return render(request,'index.html',context)