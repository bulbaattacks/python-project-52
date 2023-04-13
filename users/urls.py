from django.urls import path
from users import views


urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
]