from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from app.testcase.models import TestCaseDocument, TestCaseFunction, Trader, TestCase, TestCaseBug, TestCaseModule
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
    def get(self, request, type):
        if type == '0':
            data = Trader.objects.all()
        else:
            data = Trader.objects.filter(type=type).all()
        json_data = []
        for item in data:
            json_data.append({'logo': item.logo, 'code': item.code, 'name': item.name, 'type': item.type})
        return JsonResponse({'code': 100, 'message': json_data})


class TestCaseTempletView(LoginRequiredMixin, View):
    pass


class TestCaseListView(LoginRequiredMixin, View):

    def get(self, request, trade_code):
        jsondata = []
        trader = Trader.objects.get(code=trade_code)
        data_list = TestCase.objects.filter(trader=trader).all()
        for item in data_list:
            bugs = TestCaseBug.objects.filter(test_case=item)
            jsondata.append({
                'bugnum': len(bugs),
                'phone_system': item.phone_system,
                'date': item.create_time,
                'status': item.result,
                'id': item.id,
                'content': item.module.name
            })

        return JsonResponse({'code': 100, 'message': jsondata})


class TestCaseView(LoginRequiredMixin, View):
    pass

class TestCaseBugListView(LoginRequiredMixin, View):
    pass


class TestCaseBugView(LoginRequiredMixin, View):
    pass
