from django.urls import path,re_path
from DjangoAPI.settings import MEDIA_ROOT, MEDIA_URL
# from django.conf.urls import re_path as url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # url(r'^department/$',views.departmentApi),
    # url(r'^department/([0-9]+)',views.departmentApi)
    re_path(r'^department/$',views.departmentApi),
    re_path(r'^department/([0-9]+)',views.departmentApi),

    re_path(r'^employee/$',views.employeeApi),
    re_path(r'^employee/([0-9]+)',views.employeeApi),

    re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
