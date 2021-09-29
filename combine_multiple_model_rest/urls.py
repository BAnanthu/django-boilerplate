from django.urls import path

from .import views


urlpatterns = [
    path('post-two-model/', views.CombineModelPost.as_view())
]