from django.shortcuts import render
from . import forms
from basicapp.models import Contact_Info

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            #DO SOMETHING....

            print("Validation success!!")
            print("Name:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("Text:"+form.cleaned_data['text'])

            insert_me = Contact_Info(name= form.cleaned_data['name'], email = form.cleaned_data['email'], text = form.cleaned_data['text'])
            insert_me.save()
            print("The data has been written to the database")

    return render(request, 'basicapp/form_page.html',{'form':form})


