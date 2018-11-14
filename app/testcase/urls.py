from django.urls import re_path

from app.testcase.views import TestCaseTempletListView, TestCaseTempletView, TestCaseListView, TestCaseView, \
    TestCaseBugListView, TestCaseBugView, IndexView,TraderView

app_name = 'testcase'
urlpatterns = [
    re_path(r'^index$', IndexView.as_view(), name='index'),
    re_path(r'^trader/(?P<type>\d+)', TraderView.as_view(), name='trader'),
    # re_path(r'^test_case', TestCaseView.as_view(), name='test_case'),
    # re_path(r'^test_case_bug_list', TestCaseBugListView.as_view(), name='test_case_bug_list'),
    # re_path(r'^test_case_bug', TestCaseBugView.as_view(), name='test_case_bug'),
    # re_path(r'^test_case_templet_list/(?P<doc_name>\d+)/(?P<page>\d+)', TestCaseTempletListView.as_view(), name='test_case_templet_list'),
    # re_path(r'^test_case_templet', TestCaseTempletView.as_view(), name='test_case_templet'),
]
