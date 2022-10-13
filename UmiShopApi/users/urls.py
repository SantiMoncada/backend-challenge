from django.urls import path
from users import views

urlpatterns = [
    path('user', views.user_list),
    path('user/<int:pk>', views.user_details),
    path('user/registered/<str:email>', views.user_is_registered)
]
