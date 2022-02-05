from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import myuser,students


# Create your views here.
def register(request):
    context = {}
    if(request.method=='GET'):
        return  render(request,'register.html')
    else:
        print(request.POST)
        myuser.objects.create(username=request.POST['username'],password=request.POST['password'])
        user = myuser.objects.all()
        return redirect('/login',{'users':user})

def login(request):
    context = {}
    if(request.method=='GET'):
        context['users']=myuser.objects.all()
        return render(request, 'login.html',context)
    else:
        print(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        print(username)

        user= myuser.objects.filter(username=username,password=password)
        print(user)
        if(len(user)>0):
            user=user[0]
        if(user):
            print("in")
            return redirect('/home')
        else:
            context['errormsg']='Invalid credentials.'
            return render(request, 'login.html', context)


def home(request):
    return render(request,'home.html')

def addstudent(request):
    if (request.method == 'GET'):
        return render(request, 'addstudent.html')
    else:
        print(request.POST)
        students.objects.create(name=request.POST['name'], track=request.POST['track'])
        stud = students.objects.all()

        return redirect('/addstu', {'student': stud})

def update(request):
    if request.method =='GET':
        return render(request,'update.html')
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        track = request.POST.get('track')
        student = students.objects.filter(id=id)
        student.update(name=name, track=track)
        return render(request, 'update.html')


def deletestu(request):
    if request.method =='GET':
        return render(request,'delete.html')
    else:
        id = request.POST.get('id')
        student = students.objects.filter(id=id)
        student.delete()
        return render(request,'delete.html')

def select(request):
    if request.method =='GET':
        context={}
        context['students']=students.objects.all()
        print(context['students'])

        return render(request,'select.html',context)


def search(request):
    if request.method =='GET':

        return render(request,'search.html')
    else:
        name = request.POST.get('name')
        context={}
        context['students']=students.objects.filter(name=name)

        return render(request,'search.html',context)
       









    




