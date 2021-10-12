from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', views.loginView, name='login'),
    path('password-reset/', views.passwordResetView, name="password_reset"),
    path('password-reset/done/', views.passwdResetDoneView, name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', views.passwadResetConfirmView, name="password_reset_confirm"),
    path('password-reset/complete/', views.passwordResetCompleteView, name="password_reset_complete"),
]
