from django.shortcuts import render, redirect
from django.contrib.auth import login, views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
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


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

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

passwordChangeView = auth_views.PasswordChangeView.as_view(
                template_name='accounts/passwd/password_change.html')

passwordChangeDoneView = auth_views.PasswordChangeDoneView.as_view(
                template_name='accounts/passwd/password_change_done.html')
