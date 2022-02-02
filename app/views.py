import email
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request, "app/insert.html")

def InsertData(request):
    #data come from insert.html to views.py
    fname = request.POST.get('fname', False)
    lname = request.POST.get('lname', False)
    email = request.POST.get('email', False)
    contact = request.POST.get('contact', False)

    #creating object of model class
    #inserting data to table
    newuser= Student.objects.create(firstname=fname, lastname=lname, email=email, contact=contact)

    #after insert render on show 
    return redirect('Showpage')

#Show data view
def ShowPage(request):
    #select * from tablename
    #for fetching all the data from table
    all_data =  Student.objects.all()
    return render(request,"app/show1.html",{'key1':all_data})


#Edit view
def EditPage(request,pk):
    #fetching the data of particular id
    get_data= Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})


#Updating data View
def UpdateData(request,pk):
    udata= Student.objects.get(id=pk)
    udata.firstname= request.POST['fname']
    udata.lastname= request.POST['lname']
    udata.email= request.POST['email']
    udata.contact= request.POST['contact']
    #query for update
    udata.save()
    #Render to Show page
    return redirect('Showpage')


#Delete Data view
def DeleteData(request,pk):
    ddata= Student.objects.get(id=pk)
    #query for delete
    ddata.delete()
    return redirect('Showpage')


#Adding data view
def Add(request):
    return render(request, "app/insert.html")
