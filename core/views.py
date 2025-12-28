from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from core.forms import StudentForm
from core.forms import MarksForm
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,user_passes_test



def is_staff_user(user):
    return user.is_authenticated and user.is_staff

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def student_list(request):
    query = request.GET.get('q','')
    students = Student.objects.all().order_by('-created_at')
    if query:
        students = students.filter(
        Q(name__icontains=query) |
        Q(email__icontains=query) |
        Q(department__icontains=query) |
        Q(roll_number__icontains=query) 
        )
    paginator = Paginator(students,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/student_list.html', {'page_obj':page_obj,'query':query})

@login_required
@user_passes_test(is_staff_user)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'core/student_form.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'core/student_form.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(request,'Student deleted succesfully.')
        return redirect('student_list')
    
    return render(request,'core/student_confirm_delete.html',{'student':student})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request, 'core/student_detail.html', {'student':student})


@login_required
@user_passes_test(is_staff_user)
def marks_create(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = MarksForm()
    return render(request, 'core/marks_form.html',{'form':form})

def student_report(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks = student.marks.select_related('subject')

    context = {
        'student': student,
        'marks': marks,
    }
    return render(request, 'core/student_report.html', context)


