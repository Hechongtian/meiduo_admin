from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.utils import timezone

from users.models import User

# 日活跃用户统计
# GET /meiduo_admin/statistical/day_active/
class UserDayActiveView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取日活用户量:
        1. 获取日活用户量
        2. 返回应答
        """
        # 1. 获取日活用户量
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()

        # 2. 返回应答
        response_data = {
            'date': now_date.date(),
            'count': count
        }

        return Response(response_data)

# 日下单用户统计
# GET /meiduo_admin/statistical/day_orders/
class UserDayOrdersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取日下单用户数量：
        1. 获取日下单用户数量
        2. 返回应答
        """
        # 1. 获取日下单用户数量
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()

        # 2. 返回应答
        response_data = {
            'date': now_date.date(),
            'count': count
        }

        return Response(response_data)

# 30天新增用户统计
# GET /meiduo_admin/statistical/month_increment/
class UserMonthCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取当月每日新增用户数据:
        1. 获取当月每日新增用户数据
        2. 返回应答
        """
        # 1. 获取当月每日新增用户数据
        # 结束时间
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 起始时间: now_date - 29天
        begin_date = now_date - timezone.timedelta(days=29)

        # 当天日期
        current_date = begin_date

        # 新增用户的数量
        month_li = []

        while current_date <= now_date:
            # 次日时间
            next_date = current_date + timezone.timedelta(days=1)
            # 统计当天的新增用户数量
            count = User.objects.filter(date_joined__gte=current_date,
                                        date_joined__lt=next_date).count()

            month_li.append({
                'count': count,
                'date': current_date.date()
            })

            current_date += timezone.timedelta(days=1)

        # 2. 返回应答
        return Response(month_li)
