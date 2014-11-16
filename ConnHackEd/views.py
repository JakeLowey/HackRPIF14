from django.shortcuts import render_to_response

# Create your views here.


def login_url(request):
    return render_to_response('registration/login.html')