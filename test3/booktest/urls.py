from django.conf.urls import include,url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), # 首页
    # url(r'^showarg(\d+)$', views.show_arg), # 捕获url参数：位置参数
    url(r'^showarg(?P<num>\d+)$', views.show_arg), # 捕获url参数：关键字参数（关键字必须与视图中的参数保持一致）
    url(r'^login$', views.login), # 显示登录页面
    url(r'^login_check$', views.login_check), # 用户登录校验

    url(r'^ajax_test$', views.ajax_test), # 显示ajax页面
    url(r'^ajax_handle$', views.ajax_handle), # ajax处理

    url(r'^login_ajax$', views.login_ajax), # 显示ajax登录页面
    url(r'^login_ajax_check$', views.login_ajax_check), #ajax登录校验

    url(r'set_cookie$', views.set_cookie), #设置cooki
    url(r'get_cookie$', views.get_cookie), #获取cookie

    url(r'^set_session$', views.set_session), #设置session
    url(r'^get_session$', views.get_session), #获取session
]