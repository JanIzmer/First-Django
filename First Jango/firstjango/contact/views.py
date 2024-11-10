from django.shortcuts import render

def ContactView(request):
    return render(request, "contact/contact.html")
