from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.MyLogin.as_view(), name="login"),
    path('change_password/', views.ChangeMyPassword.as_view(), name="change_password"),
    path('change_password_done/', views.ChangeMyPasswordDone.as_view(),name="change_password_done"),
    path('logout/', views.LogOutMe.as_view(), name="logout"),
    path('<int:pk>-update/', views.EditAccount.as_view(), name="update"),
    path('create-account/', views.CreateNewAccount.as_view(), name="create"),
    path('reset_password/', views.MyPasswordReset.as_view(), name="password_reset"),
    path('reset_password-done/', views.MyPasswordResetConfirm.as_view(), name="password_reset_confirm"),
]