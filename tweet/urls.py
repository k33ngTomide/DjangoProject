from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from rest_framework_nested.routers import NestedDefaultRouter

from . import views
from .views import CommentViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register('tweets', views.TweetViewSet, basename='tweets')

comment_router = (routers.NestedDefaultRouter(router, "tweets", lookup="tweet"))
comment_router.register('comments', CommentViewSet, basename="tweets-comments")

urlpatterns = router.urls + comment_router.urls

# urlpatterns = [
#     path(r'', include(router.urls)),
#     path(r'', include(comment_router.urls)),

    # path('', views.TweetCreate.as_view()),
    # path('<int:pk>/', views.TweetDetailsView.as_view()),
    # path('comments/<int:pk>/', views.CommentDetailsView.as_view()),
    # path('comments/', views.CommentCreate.as_view()),
# ]


