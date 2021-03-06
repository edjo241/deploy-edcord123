from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.home,name='home'),
    path('room/<str:pk>',views.room,name='room'),
    path('user-profile/<str:pk>',views.UserProfile,name='user-profile'),
    path('create-room/',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>',views.UpdateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.DeleteRoom,name='delete-room'),
    path('delete-message/<str:pk>',views.DeleteMessage,name='delete-message'),
    path('register/',views.registerUser,name='register'),
    path('update-user/',views.UpdateUser,name='update-user'),
    path('topics/',views.TopicPage,name='topics'),
    path('activity/',views.ActivityPage,name='activity'),
    
    
]