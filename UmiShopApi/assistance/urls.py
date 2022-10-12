from django.urls import path
from assistance import views

urlpatterns = [
    path('assistance/', views.assistance),
]
