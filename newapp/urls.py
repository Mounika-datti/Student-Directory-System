from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='logo'),
    path('admin.html/',views.admin,name='admin'),
    path('about_us/',views.about_us,name='about'),
    path('studenthomepage/',views.studenthome,name='stuhome'),
    path('add.html/',views.add_student,name='add'),
    path('students/', views.student_list, name='student_list'),
    path('student/delete/', views.delete_student, name='delete_student'),
    path('student/edit/<str:roll_no>/', views.edit_student, name='edit_student'),
     path('search/', views.search_students, name='search_students'),
    path('search/results/', views.search_results, name='search_results'),
    path('signup/', views.signup_view, name='signup'),
    path('signup/success/', views.signup_success_view, name='signup_success'),
    path('profile/', views.view_profile, name='view_profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('reports/', views.reports_page, name='reports_page'),
]