from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import * 


# Create your views here.
def index(request):
    return render(request,'index.html')