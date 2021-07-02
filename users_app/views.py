from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    context = {
        "allUsers": User.objects.all()
    }
    return render(request, "index.html", context)



# you gonna need 2 methods one to post to db another to retrieve

def addUserdb(request):
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age']
    )
    return redirect('/')
