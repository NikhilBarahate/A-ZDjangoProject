from unicodedata import name
from django.urls import path
from app1.views import employeeView, showEmployeeView, deleteView, updateView

urlpatterns = [
    path('emp/', employeeView, name="emp_urls"),
    path('se/', showEmployeeView, name="showemp_urls"),
    path('dl/<int:id>/', deleteView, name='delete_urls'),
    path('up/<int:id>/', updateView, name='update_urls'),

]