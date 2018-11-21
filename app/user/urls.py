from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required

from app.user.views import LoginView, LogoutView, TeamView

app_name = 'user'
urlpatterns = [
    re_path(r'^login$', LoginView.as_view(), name='login'),
    re_path(r'^logout$', LogoutView.as_view(), name='logout'),
    re_path(r'^team', TeamView.as_view(), name='team'),
]
