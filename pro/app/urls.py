from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("emp/",views.emp_list, name="emp"),
    path("emp/<int:id>",views.emp_detail, name="emp-id"),
    # path('employees/add/', views.emp_list, name='emp-add'),
    
]

urlpatterns=format_suffix_patterns(urlpatterns)