from django.urls import re_path

from app.testcase.views import TestCaseTempletListView, TestCaseTempletView, TestCaseListView, TestCaseView, \
    TestCaseBugListView, TestCaseBugView, IndexView, TraderView, TestCaseDetailView

app_name = 'testcase'
urlpatterns = [
    re_path(r'^index$', IndexView.as_view(), name='index'),
    re_path(r'^trader/(?P<type>\d+)', TraderView.as_view(), name='trader'),
    re_path(r'^list/(?P<trade_code>\d+)', TestCaseListView.as_view(), name='testcase_list'),
    re_path(r'^detail/(?P<test_case_id>\d+)', TestCaseDetailView.as_view(), name='testcase_detail'),
    re_path(r'^bug/(?P<bug_id>\d+)', TestCaseBugView.as_view(), name='testcase_bug'),
]
