from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import render , redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import*
from datetime import date

def coustmer_front(request):
    return render(request, 'front.html') 

    
def coustmer_signup(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                messages.error(request, 'enter password do not match please try again!')
                return redirect('signup')
            if len(password1) < 8:
                messages.error(request, 'password length must be 8 character!')
                return redirect('signup')
            myuser = User.objects.create_user(username,email,password1)
            myuser.save()
            messages.success(request, "account created now click on login button to enter the website")
            return redirect('signup') 
        return render(request, 'signup.html')   
    except Exception as E:
        return HttpResponse(request, str(E))
    

def coustmer_login(request):
    try:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            myuser = authenticate(username=username,password=password)
            if myuser is not None:
                login(request,myuser)
                messages.success(request, 'login sucessfully !!!!')
                return redirect('showimage')
            else:
                messages.error(request, "given details not match we can't cotinue your Login Please check details and try again to Login!")
                return redirect('login')
        return render(request, 'login.html') 
    except Exception as E:
        return HttpResponse(request, str(E))   


def coustmer_preview(request,id):
    if id == 1:
        return render(request,'proposal1.html')
    if id == 2:
        return render(request,'proposal2.html')
    if id == 3:
        return render(request,'proposal3.html')


def create_proposal(request,id):
    if request.method == 'POST':
        a = request.user
        title = request.POST['title']
        companyname = request.POST['companyname']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        proposalsummary = request.POST['summary']
        projectplanning = request.POST['planning']
        financing = request.POST['financing']
        additionalcustomsections = request.POST['information']
        created_at = request.POST['date']
        data = CoustmerDetail(title=title,companyname=companyname,name=name,email=email,contact=contact,proposalsummary=proposalsummary,
        projectplanning=projectplanning,financing=financing,additionalcustomsections=additionalcustomsections,created_at=created_at,user_id=a.id)
        data.save()
        return redirect('showimage')
    return render(request,'form.html')


def coustmer_after_create(request,id):
    data = CoustmerDetail.objects.get(id=id)
    data_dict = {'showdata' : data}
    if data.templatesdetail.id == 1:
        return render(request,'aftercreate1.html',data_dict)
    if data.templatesdetail.id == 2:
        return render(request,'aftercreate2.html',data_dict)
    if data.templatesdetail.id == 3:
        return render(request,'aftercreate3.html',data_dict)
    

def edit_proposal(request, id):
    data = CoustmerDetail.objects.get(id = id)
    data_dict = {'editdata' : data}
    if request.method == "POST":
        title = request.POST['title']
        companyname = request.POST['companyname']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        proposalsummary = request.POST['summary']
        projectplanning = request.POST['planning']
        financing = request.POST['financing']
        additionalcustomsections = request.POST['information']
        created_at = request.POST['date']
        data.title = title
        data.companyname = companyname
        data.name = name
        data.email = email
        data.contact = contact
        data.proposalsummary = proposalsummary
        data.projectplanning = projectplanning
        data.financing = financing
        data.additionalcustomsections = additionalcustomsections
        data.created_at = created_at
        data.save()
        return redirect('showimage')
    return render(request, 'edit.html', data_dict)


def delete_proposal(request,id):
    data = CoustmerDetail.objects.get(id = id)
    data.delete()
    return redirect('showimage')


def coustmer_proposal_image(request):
    data = TemplatesName.objects.all()
    data1 = CoustmerDetail.objects.filter(user__id=request.user.id)    
    context = {
            'showimage':data,
            'showdata' : data1,
    }
    return render(request,'afterlogin.html',context)

     
 
def coustmer_logout(request):
    logout(request)
    messages.success(request, 'logout sucessfully !!!')
    return redirect('front')

