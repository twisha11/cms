from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:slug>', views.detail, name = 'detail'),
    path('create-post',views.createPost,name='createpost'),
    path('update-post/<str:slug>',views.updatePost,name='update'),
    path('delete-post/<str:slug>',views.deletePost,name='delete'),
    path('register',views.register_page,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('search/', views.search, name='search'),
    path('category/<str:slug>', views.category, name='category'),

]