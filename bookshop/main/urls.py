from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.ViewMain.as_view(), name="main"),
    path('staff-admin/', views.ViewStaffPage.as_view(), name="staff_page"),
]
