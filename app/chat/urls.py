from django.urls import re_path

from app.chat import views
from app.testcase.views import TestCaseTempletListView, TestCaseTempletView, TestCaseListView, TestCaseView, \
    TestCaseBugListView, TestCaseBugView, IndexView, TraderView, TestCaseDetailView

app_name = 'chat'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^taskfinish$', views.taskfinish, name='taskfinish'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
