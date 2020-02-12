from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from goods.models import SPU
from meiduo_admin.serializers.spus import SPUSimpleSerializer


# GET /meiduo_admin/goods/simple/
class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    # 指定视图使用的查询集
    queryset = SPU.objects.all()
    # 指定视图使用的序列化器类
    serializer_class = SPUSimpleSerializer

    # 注：关闭分页
    pagination_class = None
