from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Students

# Create your views here.
def student_list(request):
    students=Students.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_create(request):
    if request.method=='POST':
        fName=request.POST['first_name']
        lName=request.POST['last_name']
        email=request.POST['email']
        ph_no=request.POST['phone_number']
        dob=request.POST['date_of_birth']

        Students.objects.create(
            first_name=fName,
            last_name=lName,
            email= email,
            phone_number=ph_no,
            date_of_birth=dob
        )
        return redirect('student_list')
    return render(request,'student_form.html')




def student(request):
    return render(request,'portfolio.html')

def profile(request):
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')

     