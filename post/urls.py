from .views import CreatePostView,ListPostView,DetailPostView,DeletePostView,UpdatePostView,SearchPostView,ProfilPostView,CreateCommentView
from django.urls import path,re_path


urlpatterns= [
     path('post/new/', CreatePostView.as_view(), name='create_post'),
     path('', ListPostView.as_view(), name='home'),
     path('post/<slug:slug>/',DetailPostView.as_view(),name='post_detail'),
     path('post/<slug:slug>/delete',DeletePostView.as_view(),name='post_delete'),
     path('post/<slug:slug>/update',UpdatePostView.as_view(),name='post_edit'),
     path('post/search_list', SearchPostView.as_view(), name='search_list'),
     path('post/<slug:slug>/profile', ProfilPostView.as_view(), name='profile'),
     path('post/<slug:slug>/comment',CreateCommentView.as_view(),name='create_comment'),

]