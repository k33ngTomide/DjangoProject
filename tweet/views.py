from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentViewSet(ModelViewSet):
    # queryset = Comment.objects.select_related('tweet').all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.select_related("tweet").filter(tweet_id=self.kwargs['tweet_pk'])
        return queryset

# class TweetCreate(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
# class TweetDetailsView(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer


# class CommentCreate(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentDetailsView(RetrieveDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# def perform_destroy(self, instance):
#     print(self.get_object())
#     if self.get_object().tweet == self.request.user:
#         instance.delete()

# def register(request):
#     if request.method == 'POST':
#         data = request.data
#         serializer = CommentSerializer(data=data)
