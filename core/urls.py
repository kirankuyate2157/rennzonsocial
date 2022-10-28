from . import views
from django.urls import path

urlpatterns =[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('upload',views.upload,name='upload'),
    path('logout',views.logout,name='logout'),
    path('settings',views.setting,name='setting'),
]