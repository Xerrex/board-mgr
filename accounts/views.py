from django.shortcuts import render

def signup(request):
    """Handle user signing up operations
    """
    return render(request, "accounts/signup.html")
