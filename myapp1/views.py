from django.shortcuts import redirect, render
from myapp1.forms import ChangePassForm, LoginForm, RegisterForm, UpdateForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

from myapp1.models import Gallery, RegTable

# Create your views here.

# Index Page
def index(request):
    return render(request, 'index.html')


# Register
def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST,request.FILES)

        if reg_form.is_valid():
            # Email and Password validation 
            name = reg_form.cleaned_data['Name']
            age = reg_form.cleaned_data['Age']
            place = reg_form.cleaned_data['Place']
            photo = reg_form.cleaned_data['Photo']
            email = reg_form.cleaned_data['Email']
            password = reg_form.cleaned_data['Password']
            cpassword = reg_form.cleaned_data['ConfirmPassword']

            user = RegTable.objects.filter(Email = email)
            if user :
                messages.warning(request,'Email alredy exists')
                return redirect('/register')

            elif password!=cpassword :
                messages.warning(request,'Password Missmatched')
                return redirect('/register')
            
            else:
                reg = RegTable(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                reg.save()
                messages.success(request, 'Registered Successfully')
                return redirect('/')

    else:
        reg_form = RegisterForm()
    return render(request, 'register.html', {'reg_form':reg_form})


# Login
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid(): 
            # Email and Password validation 
            email = login_form.cleaned_data['Email'] 
            password = login_form.cleaned_data['Password'] 

            user = RegTable.objects.get(Email = email)
            if not user :
                messages.warning(request,'Email doesnot exists')
                return redirect('/login')

            elif password != user.Password :
                messages.warning(request,'Password Incorrect')
                return redirect('/login')
            
            else:
                messages.success(request, 'Logined Successfully')
                return redirect('/home/%s' % user.id)

    else:
        login_form = LoginForm() 
    return render(request, 'login.html', {'login_form':login_form}) 


# View user
def home(request,id):
    user = RegTable.objects.get(id = id)
    return render(request, 'home.html', {'user':user})


# Change Password
def changepass(request,id):
    user = RegTable.objects.get(id = id)
    if request.method == 'POST':
        chg_form = ChangePassForm(request.POST)

        if chg_form.is_valid():
            oldpassword = chg_form.cleaned_data['OldPassword']
            newpassword = chg_form.cleaned_data['NewPassword']
            cpassword = chg_form.cleaned_data['ConfirmPassword']

            if oldpassword != user.Password :
                messages.warning(request,'Incorrect Password')
                return redirect('/changepass/%s' % user.id)

            elif oldpassword == newpassword :
                messages.warning(request,'Password Similar')
                return redirect('/changepass/%s' % user.id)
            
            elif newpassword != cpassword :
                messages.warning(request,'Password Missmatch')
                return redirect('/changepass/%s' % user.id)

            else :
                user.Password = newpassword
                user.save()
                messages.success(request,'Password Changed...')
                return redirect('/')

    else:
        chg_form = ChangePassForm()
    return render(request,'changepass.html',{'chg_form':chg_form,'user':user})


# Update user
def update(request,id):
    user = RegTable.objects.get(id = id)
    if request.method == 'POST':
        udt_form = UpdateForm(request.POST or None, instance = user)
        
        if udt_form.is_valid():
            udt_form.save()
            messages.success(request, 'Update Successfull')
            return redirect('/login')

    else:
        udt_form = UpdateForm(instance = user)
    return render(request, 'update.html', {'udt_form':udt_form, 'user':user})


# Logout
def logout(request):
    logouts(request)
    messages.success(request, 'Logouted Successfully')
    return redirect('/')


# Gallery 
def gallery(request):
    allimg = Gallery.objects.all()
    return render(request, 'gallery.html' , {'allimg':allimg})


# View Image Details
def view_details(request,id):
    view = Gallery.objects.get(id = id)
    return render(request, 'view_details.html', {'view':view})