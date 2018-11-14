from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View


class LoginView(View):
    def get(self, request):
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})
        # 业务逻辑
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名密码正确
            # 记录用户的登录状态
            login(request, user)
            # 获取登录后所要跳转的地址
            # 默认跳转到首页
            # 如果是require_login返回的url：http://127.0.0.1:8000/user/login?next=/user/
            # 有一个登录成功后要跳转的页面，k:next v:/user/
            next_url = request.GET.get('next', reverse('testcase:index'))  # 第二个参数是默认值
            # 跳转到next_url
            response = redirect(next_url)
            # 判断是否记住用户名
            remember = request.POST.get('remember')

            if remember == 'on':
                response.set_cookie('username', username, max_age=7 * 24 * 3600)
            else:
                response.delete_cookie('username')
            # 返回response
            return response

        else:
            return render(request, 'login.html', {'errmsg': '用户密码错误'})


class LogoutView(View):
    def get(self, request):
        # 清除用户的session信息
        logout(request)
        # 跳转到首页
        return redirect(reverse('testcase:index'))
