from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

login_view = auth_views.LoginView.as_view(template_name='accounts/login.html')


password_reset_view = auth_views.PasswordResetView.as_view(
    template_name='accounts/password_reset.html',
    email_template_name='accounts/password_reset_email.html',
    subject_template_name='accounts/password_reset_subject.txt'
)

password_reset_done_view = auth_views.PasswordResetDoneView.as_view(
    template_name='accounts/password_reset_done.html'
)


password_reset_confirm_view = auth_views.PasswordResetConfirmView.as_view(
    template_name='accounts/password_reset_confirm.html'
)

password_reset_complete_view = auth_views.PasswordResetCompleteView.as_view(
    template_name="accounts/password_reset_complete.html"
)

password_change_view = auth_views.PasswordChangeView.as_view(
    template_name="accounts/password_change.html"
)


password_change_done_view = auth_views.PasswordChangeDoneView.as_view(
    template_name="accounts/password_change_done.html"
)

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", login_view, name="login"),

    path("reset/", password_reset_view, name="password_reset"),
    path("reset/done/", password_reset_done_view, name="password_reset_done"),
    path("reset/<uidb64>/<token>/", password_reset_confirm_view, name="password_reset_confirm"),
    path("reset/complete/", password_reset_complete_view, name="password_reset_complete"),
    path("settings/password/", password_change_view, name="password_change"),
    path("settings/password/done", password_change_done_view, name="password_change_done")
]


# PasswordResetView:email
# PasswordChangeView:loggedIn Users

# PasswordResetDoneView:email
# PasswordChangeDoneView:loggedIn Users

# PasswordResetConfirmView
# PasswordResetCompleteView

