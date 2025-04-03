from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.contrib import messages
from django.http import JsonResponse
from .forms import EditStudentForm 
from django.db.models import Q
def home(request):
    return render(request,"home.html")
def admin(request):
    return render(request,"admin.html")
def studenthome(request):
    return render(request,"student.html")
def login(request):
    return render(request,"login.html")
def about_us(request):
    return render(request,"aboutus.html")
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        roll_no = request.POST['roll_no']
        department = request.POST['department']
        year_of_study = request.POST['year_of_study']
        email = request.POST['email']
        phone = request.POST['phone']

        try:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                roll_no=roll_no,
                department=department,
                year_of_study=year_of_study,
                email=email,
                phone=phone
            )
            messages.success(request, 'Student added successfully!')
            return redirect('student_list') # Redirect to the student list page
        except Exception as e:
            messages.error(request, f'Error adding student: {e}')
            return render(request, 'add.html') # Re-render the form with error message
    else:
        return render(request, 'add.html') 

def student_list(request):
    """Renders the list of all students."""
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})

def delete_student(request):
    """Handles the deletion of a student via AJAX."""
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        if roll_no:
            try:
                student = get_object_or_404(Student, roll_no=roll_no)
                student.delete()
                return JsonResponse({'status': 'success', 'message': f'Student with Roll No: {roll_no} deleted successfully.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Error deleting student: {str(e)}'}, status=500)
        else:
            return JsonResponse({'status': 'error', 'message': 'Roll No not provided.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
def edit_student(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student) # Populate form with existing instance
        if form.is_valid():
            form.save()
            return redirect('student_list') # Redirect after successful edit
    else:
        form = EditStudentForm(instance=student) # Populate form for GET request
    return render(request, 'edit.html', {'student': student, 'form': form})

def search_students(request):
    """Renders the search students form."""
    return render(request, 'search.html')

def search_results(request):
    """Handles the search query and displays results."""
    searched = True
    results = []
    if request.method == 'GET':
        name = request.GET.get('name', '')
        rollno = request.GET.get('rollno', '')
        department = request.GET.get('department', '')

        query = Q()

        if name:
            query &= Q(first_name__icontains=name) | Q(last_name__icontains=name)
        if rollno:
            query &= Q(roll_no__icontains=rollno)
        if department:
            query &= Q(department__icontains=department)

        results = Student.objects.filter(query)

    context = {
        'search_results': results,
        'searched': searched,
    }
    return render(request, 'search.html', context)

def signup_view(request):
    if request.method == 'POST':
        # Process the form data here
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        birthday = request.POST.get('birthday')
        location = request.POST.get('location')
        terms = request.POST.get('terms')  # This will be 'on' if checked

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signin.html')

        # In a real application, you would:
        # 1. Validate the data (e.g., using Django forms).
        # 2. Create a new user in your database.
        # 3. Potentially send a verification email.
        # 4. Redirect the user to a success page or log them in.

        messages.success(request, "Account created successfully!")
        return redirect('signup_success') # You'd need to define this URL

    else:
        # If it's a GET request, just display the form
        return render(request, 'cprofile.html')

def signup_success_view(request):
    return render(request, 'cprofile.html') # Create this template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def view_profile(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        # Handle the case where a profile hasn't been created yet
        user_profile = UserProfile(user=request.user)
        user_profile.save()  # Or redirect to a create profile page

    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages

@login_required
def edit_profile_view(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        user.save()

        user_profile.birthday = request.POST.get('birthday')
        user_profile.location = request.POST.get('location')
        user_profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('view_profile')
    else:
        context = {'user_profile': user_profile}
        return render(request, 'edit_profile.html', context)

def reports_page(request):
    return render(request, 'reports.html')