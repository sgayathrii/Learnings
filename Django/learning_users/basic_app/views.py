from django.shortcuts import render,redirect
from basic_app.forms import UserForm, UserProfileInfoForm,LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

#by haithem
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required




# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')

#---------------------------
#Coding by haithem
@login_required
def profile(request):
    #return HttpResponse("You are logged in!, Nice!")
    args = {'user': request.user}
    return render(request, 'basic_app/profile.html', args)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#--------------------------
def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print("Found it!")
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', 
                 {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def login_page(request):
    message = ''
    
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.info(request, f'Hello {user.username}! You have been logged in')
                return redirect('/basic_app/dashboard')
            else:
                messages.error(request, "Login Failed")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = LoginForm()           
    return render(request, 'basic_app/login.html', context={'login_form': login_form})


#Logout
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('basic_app/logout.html')

#coding by haithem
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                print("You are logged in!, Nice!")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("Someone tried to log in and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render(request, 'basic_app/loginpage.html', {})
