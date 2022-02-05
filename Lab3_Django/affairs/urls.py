from django.urls import path

from affairs import views

urlpatterns = [
    path("", views.StudentV.as_view(), name="affairs"),
    path("student/", views.StudentV.as_view(), name="student"),
    path("students/", views.students, name="students"),
    path('del_student/<int:pk>', views.del_student, name="del_student"),
    path('update_student/<int:pk>', views.update_student, name="update_student")
]
