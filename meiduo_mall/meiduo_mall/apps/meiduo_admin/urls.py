from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from meiduo_admin.views import users, statistical, skus, spus
from meiduo_admin.views import permissions

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 用户管理
    url(r'^users/$', users.UserInfoView.as_view()),
    # 图片管理
    url(r'^skus/simple/$', skus.SKUSimpleView.as_view()),
    # SKU商品管理
    url(r'^goods/simple/$', spus.SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', spus.SPUSpecView.as_view()),
]

# 图片管理
router = DefaultRouter()
router.register(r'skus/images', skus.SKUImageViewSet, basename='images')
urlpatterns += router.urls

# SKU商品管理
router = DefaultRouter()
router.register('skus', skus.SKUViewSet, basename='skus')
urlpatterns += router.urls

# 权限管理
router = DefaultRouter()
router.register('permission/perms', permissions.PermissionViewSet, basename='perms')
urlpatterns += router.urls
