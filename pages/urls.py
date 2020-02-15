from django.urls import path

from .views import HomePageView, PostListingView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('myposts', PostListingView.as_view(), name='post-list'),
]
