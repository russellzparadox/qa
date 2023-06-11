from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('logout', views.logout_view),
    path('insert/', views.add_question),
    path('like/',views.likeView,name='like_question'),
]
