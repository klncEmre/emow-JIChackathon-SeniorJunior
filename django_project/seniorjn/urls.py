from django.urls import path
from .views import (

    home,
    profile_junior,
    about,
    searchBar,
    UserDetailView
)


urlpatterns = [
    path('', home, name='seniorjn-home'),
    path('user/<int:pk>', UserDetailView.as_view() , name='user-posts'),
    path('about/', about, name='seniorjn-about'),
    path('search/',searchBar,name="search"),

]