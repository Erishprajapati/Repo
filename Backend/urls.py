# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/',admin.site.urls),
    path('jobs/', JobView.as_view(), name="job"),
    path('jobs/<int:pk>',JobView.as_view(), name="job-update"),
    path('api/company/', CompanyView.as_view(), name="company"),
    path("api/application/", ApplicationView.as_view(), name="application")
]
