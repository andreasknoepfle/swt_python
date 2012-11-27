from django.conf.urls import include, patterns, url
from django.contrib import admin

from swtdemo.views import EmployeeCreate, EmployeeUpdate, EmployeeDelete

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'employee/add/$', EmployeeCreate.as_view(), name='employee_add'),
    url(r'employee/(?P<pk>\d+)/$', EmployeeUpdate.as_view(), name='employee_update'),
    url(r'employee/(?P<pk>\d+)/delete/$', EmployeeDelete.as_view(), name='employee_delete'),
)

