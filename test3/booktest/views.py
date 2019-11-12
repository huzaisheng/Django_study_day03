from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime,timedelta
# Create your views here.

def index(request):
    """首页"""
    return render(request, 'booktest/index.html')

def show_arg(request, num):

    return HttpResponse(num)

def login(requset):
    """显示登录页面"""
    # 判断用户是否登录
    if requset.session.has_key('islogin'):
        # 用户已登录，跳转到首页
        return redirect('/index')
    else:
        # 用户未登录
        # 获取cookie username
        if 'username' in requset.COOKIES:
            # 获取记住的用户名
            username = requset.COOKIES['username']
        else:
            username = ''
        return render(requset, 'booktest/login.html',{'username':username})

def login_check(request):
    # request.POST 保存的是post方式提交的参数
    # request.GET 保存的是get方式提交的参数
    # 1、获取提交的用户名和密码
    # print(type(request.POST)) # 返回的是QueryDict对象
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 2、进行登录的校验
    # 实际开发：根据用户名和密码查找数据库
    # 模拟: smart  123
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到首页
        response = redirect('/index')
        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置cookie username的过期时间为1周
            response.set_cookie('username', username, max_age=7*24*3600)

        # 记住用户登录状态
        # 只要session中有islogin，就认为用户已登录
        request.session['islogin'] = True
        return response
    else:
        return redirect('/login')

def ajax_test(request):
    """显示ajax页面"""
    return render(request, 'booktest/ajax_test.html')

def ajax_handle(request):
    """ajax请求处理"""
    # 返回的json数据
    return JsonResponse({'res':1})

def login_ajax(request):
    """显示ajax登录页面"""
    return render(request, 'booktest/login_ajax.html')

def login_ajax_check(request):
    """ajax登录校验"""
    # 1、获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2、进行校验，返回json数据
    if username == 'smart' and password == '123':
        # 用户名和密码正确
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    # 设置一个cookie信息，名字为num，值为1
    # response.set_cookie('num', 1, max_age=14*24*3600)
    response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=2))
    # 返回response
    return response

def get_cookie(request):

    """获取cookie的信息"""
    num = request.COOKIES['num']
    return HttpResponse(num)

def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = 18
    # 不设置默认为2周
    # 设置session_id cookie的过期时间 为3秒
    request.session.set_expiry(60)
    return HttpResponse('设置session')

def get_session(request):
    """获取session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))