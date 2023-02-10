from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User_data
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'newIndex.html')



def help(request):
    my_view = {'insert_view':"Hello!! This is from help view"}
    return render(request, 'help.html', context=my_view)

def users(request): 

    return render(request, 'users.html', {'data': User_data.objects.all})

def userForm(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error form invalid..")

    return render(request,'signup.html', {'form': form})






 





