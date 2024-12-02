from django.urls import path
from . import views

urlpatterns = [
    # send comment
    path('api/send', views.CommentSendView.as_view()),
    path('api/discussionforum', views.CommentDiscussionForumListView.as_view()),
    path('api/list', views.CommentListView.as_view()),
    path('api/replay', views.ReplayToCommentView.as_view()),
]
