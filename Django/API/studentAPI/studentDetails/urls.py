from django.urls import path
from studentDetails import views

urlpatterns = [
    path("",views.ListStudentAPIView.as_view(),name="student_list"),
    path("create/", views.CreateStudentAPIView.as_view(),name="create_student"),
    path("update/<int:pk>/",views.UpdateStudentAPIView.as_view(),name="update_student"),
    path("delete/<int:pk>/",views.DeleteStudentAPIView.as_view(),name="delete_student")
]