from django.shortcuts import render, redirect
from django.contrib.auth import login, views as auth_views
from .forms import SignupForm


def signup(request):
    """Handle user signing up operations
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


loginView = auth_views.LoginView.as_view(template_name='accounts/login.html')
logoutView = auth_views.LogoutView.as_view()

passwordResetView = auth_views.PasswordResetView.as_view(
    template_name='accounts/passwd/password_reset.html',
    email_template_name='accounts/passwd/password_reset_email.html',
    subject_template_name='accounts/passwd/password_reset_subject.txt'
)


passwdResetDoneView = auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/passwd/password_reset_done.html')

passwadResetConfirmView = auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/passwd/password_reset_confirm.html')

passwordResetCompleteView = auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/passwd/password_reset_complete.html')