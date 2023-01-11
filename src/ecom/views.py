from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


 


def index_page(request):
  # print(request.session.get('first_name', "unknown"))
  
  context = {
  "title":"Hello World, Welcome!!",
  "content":"Home",
  }
  if request.user.is_authenticated:
    context[ "paid_content"] = "User profile"
    print(context)
  return render(request, "home.html", context)

def about_page(request):
  context = {
  "title":"This is about page",
  "content":"About",
  }
  return render(request, "home.html", context)

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
  "title":"This is contact page",
  "content":"Contact",
  "form" : contact_form ,
  
  }


  if contact_form.is_valid():
    print(contact_form.cleaned_data)

  #to print the post request details
  # if request.method == "POST":
    # print(request.POST)
    # print(request.POST.get("fullname"))
    # print(request.POST.get("email"))
    # print(request.POST.get("content"))
  return render(request, "contact/contact.html", context)


