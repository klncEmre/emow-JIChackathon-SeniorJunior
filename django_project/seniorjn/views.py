from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView

import sys
sys.path.insert(1, '/Users/emrekilinc/Desktop/hackatho/JIC-hackathon/django_project/users')
#this should be your users folder path!!!
from users import models



def home(request):
    if request.method == "GET":
        context = {
            'posts': models.Profile.objects.filter(city="Istanbul")
        }
    else:
        context = {
            'posts': models.Profile.objects.all()
        }
    return render(request, 'htmlFiles/home.html', context)


class UserDetailView(DetailView):
    model = models.Profile

def about(request):
    return render(request, 'htmlFiles/about.html', {'title': 'About'})

def profile_junior(request, username):
    userx = User.objects.filter(username=username)
    profile = models.Profile.objects.filter(user=userx).first
    return render(request, 'htmlFiles/profil.html', {'user': profile })

def searchBar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        senior = models.Profile.objects.all().filter(major = search)

        context = {
            'posts': senior,

        }
        return render(request,'htmlFiles/home.html',context)
