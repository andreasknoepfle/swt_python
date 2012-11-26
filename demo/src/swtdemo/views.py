from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from swtdemo.models import Employee

class EmployeeCreate(CreateView):
    model = Employee

class EmployeeUpdate(UpdateView):
    model = Employee

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')

