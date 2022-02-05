from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from .forms import InsertForm
from .models import Student

class StudentV(View):

    def post(self, request):
        form = InsertForm(request.POST)
        context = {'std': "active", 'form': form}
        if form.is_valid():
            return render(request, 'affairs/student.html', context)

    def get(self, request):
        form = InsertForm()
        context = {'std': "active", 'form': form}
        return render(request, 'affairs/student.html', context)


def students(request):
    data = Student.objects.all()
    if request.method == "GET" and request.user.is_authenticated:
        user_choice = request.GET.get('choice')
        search = request.GET.get('search')
        if user_choice == 'name':
            try:
                data = Student.objects.filter(student_fname__contains=search)
            except:
                pass
        elif user_choice == "email":
            try:
                data = Student.objects.filter(student_email=search)
                print(data)
            except:
                pass
        elif user_choice == "gender":
            try:
                data = Student.objects.all().filter(student_gender=search)
            except:
                pass
    else:
        return render(request, 'affairs/students.html')

 
 
    print(data)
    return render(request, 'affairs/students.html', {"stds": "active", 'data': data})


def del_student(request, pk):
    data = Student.objects.get(student_id=pk)
    if request.method == "POST":
        data.delete()
        return redirect("students")
    return render(request, 'affairs/student/Delete.html', {'data': data})


def update_student(request, pk):
    student = Student.objects.get(student_id=pk)
    if request.method == 'POST':
        try:
            student.student_fname = request.POST.get('fname')
            student.student_lname = request.POST.get('lname')
            student.student_email = request.POST.get('email')
            student.student_gender = request.POST.get('gender')
            student.save()
        except:
            pass
        return redirect("students")
    return render(request, 'affairs/student/Update.html', {'data': student})
