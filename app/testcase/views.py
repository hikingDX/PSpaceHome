from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from app.testcase.models import TestCaseDocument, TestCaseFunction
from utils.mixin import LoginRequiredMixin


# 种类id 页码 排序方式
# restful api -> 请求一种资源
# /list?type_id=种类id&page=页码&sort=排序方式
# /list/种类id/页码/排序方式
# /list/种类id/页码?sort=排序方式
class TestCaseTempletListView(LoginRequiredMixin, View):
    def get(self, request, doc_name, page):
        data_list = TestCaseFunction.objects.filter(doucument=doc_name).all()
        # 对数据进行分页
        paginator = Paginator(data_list, 10)
        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第page页的Page实例对象
        test_case_func_page = paginator.page(page)

        print(test_case_func_page)
        context = {
            'page': test_case_func_page
        }


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class TraderView(LoginRequiredMixin, View):
    def post(self, request):
        return JsonResponse({'res': 5, 'total_count': 12, 'message': '添加成功'})

    def get(self, request):
        return JsonResponse({'res': 5, 'total_count': 12, 'message': '添加成功'})


class TestCaseTempletView(LoginRequiredMixin, View):
    pass


class TestCaseListView(LoginRequiredMixin, View):

    def get(self, request):
        data_list = TestCaseFunction.objects.all()
        # 对数据进行分页
        paginator = Paginator(data_list, 10)
        # 获取第page页的内容
        try:
            page = int(10)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第page页的Page实例对象
        test_case_func_page = paginator.page(page)

        print(test_case_func_page)
        context = {
            'page': test_case_func_page
        }
        return render(request, 'index.html')


class TestCaseView(LoginRequiredMixin, View):
    pass


class TestCaseBugListView(LoginRequiredMixin, View):
    pass


class TestCaseBugView(LoginRequiredMixin, View):
    pass
