from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
#from notifications.models import Notification

# --- POST AND COMMENT VIEWS ---

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the current user as the author
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --- FEED VIEW ---

class FeedAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()  # Must exist in CustomUser model
        return Post.objects.filter(user__in=followed_users).order_by('-created_at')


# --- LIKE / UNLIKE VIEWS ---

""" class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post) 

        if created:
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)

        return Response({'detail': 'You already liked this post.'}, status=status.HTTP_200_OK) 


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)"""
