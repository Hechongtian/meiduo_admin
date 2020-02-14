from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.permissions import PermissionSerializer

# GET /meiduo_admin/permission/perms/
class PermissionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    # 指定视图所使用的查询集
    queryset = Permission.objects.all()

    # 指定视图所使用的序列化器类
    serializer_class = PermissionSerializer
