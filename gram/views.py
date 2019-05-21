from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import *

def index(request):
    images = Image.objects.all()
    # user = User.objects.get(id=id)
    return render(request,'index.html', {"images": images})

def register(request):
   if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Your account has been created! You are now able to log in')
           return redirect('login')
   else:
       form = UserRegisterForm()
   return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'register/profile.html')






































# from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
# from .models import *
# from .forms import * 
# from django.http  import HttpResponse,Http404
# # from django.http import Http404,JsonResponse, HttpResponseRedirect
# from django.contrib.auth.models import User


# # Create your views here.
# @login_required(login_url='/accounts/login')


# @login_required(login_url='/accounts/login')
# def profile(request):
#     context = {
#         'images':Image.objects.all()
#     }
#     return render(request, ('gram/profile.html'), context)

# @login_required(login_url='/accounts/login')
# def search(request):

#     if 'profile' in request.GET and request.GET["profile"]:
#         search_term = request.GET.get("profile")
#         searched_profiles = Profile.search_by_profile_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'registration/search.html',{"message":message,"profiles": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'registration/search.html',{"message":message})


# def profile(request, id):
#     user = User.objects.get(id=id)
#     followers = user.user_followers.all()
#     followers_arr = []
#     for follower in followers:
#         followers_arr.append(follower.followed_by.id)

#     if request.user.id in followers_arr:
#         is_following = True
#     else:
#         is_following = False

#     if request.user.id == int(id):
#         return redirect("profile")
#     else:
#         return render(request, "profile.html", {"user": user, "current_user": request.user, "is_following": is_following})



# def add_image(request):
#     user = request.user
#     if request.method == "POST":
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.user = user
#             image.save()
#             return redirect("index")
#     else:
#         form = ImageForm()
#     return render(request, "add_image.html", {"form": form})



# def comment(request):
#     image_id = request.POST.get("id")
#     image = Image.objects.get(pk=image_id)
#     Comments.objects.create(user=request.user, image=image,
#                             comm=request.POST.get("comment"))

#     user = request.user.username
#     comment = request.POST.get("comment")

#     data = {"user": user, "comment": comment}
#     return JsonResponse(data)



# def like(request):
#     user = request.user
#     images = Image.objects.all()
#     image_id = request.POST.get("id")

#     if user in image.likes.all():
#         image.likes.remove(user)
#         to_red = 0

#     else:
#         image.likes.add(user)
#         to_red = 1
#         likes = image.likes.all().count()
#         data = {"likes": likes, "to_red": to_red}
#     return JsonResponse(data)    



