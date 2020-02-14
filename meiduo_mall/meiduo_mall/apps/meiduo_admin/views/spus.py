from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from goods.models import SPU, SPUSpecification
from meiduo_admin.serializers.spus import SPUSimpleSerializer, SPUSpecSerializer


# 获取spu简单数据
# GET /meiduo_admin/goods/simple/
class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    # 指定视图使用的查询集
    queryset = SPU.objects.all()
    # 指定视图使用的序列化器类
    serializer_class = SPUSimpleSerializer

    # 注：关闭分页
    pagination_class = None

# 获取spu商品规格信息
# GET meiduo_admin/goods/(?P<pk>\d+)/specs/
class SPUSpecView(ListAPIView):
    permission_classes = [IsAdminUser]

    # 指定序列化器类
    serializer_class = SPUSpecSerializer

    def get_queryset(self):
        """返回视图所使用的查询集"""
        # 获取pk
        pk = self.kwargs['pk']
        return SPUSpecification.objects.filter(spu_id=pk)

    # 注：关闭分页
    pagination_class = None
