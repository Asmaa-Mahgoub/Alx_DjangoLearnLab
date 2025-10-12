from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, FollowUserView, UnfollowUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
   path("register/", UserListCreateView.as_view(), name='user-list-create'),
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/<int:pk>/", UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name='follow-user'),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name='unfollow-user'),
]