from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib import auth

from django.http import HttpRequest, HttpResponseRedirect


def authView(request: HttpRequest):

    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})
    

def logout(request: HttpRequest):

    if request.method == "POST":
        auth.logout(request)
        return redirect("login")
    else:
        return render(request, "registration/logout.html")
