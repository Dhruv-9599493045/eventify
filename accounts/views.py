from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from organizations.models import Organization

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == 'organization':
                Organization.objects.create(user=user, org_name = user.username )
            login(request,user)
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request, 'accounts/signup.html' , {'form':form})


