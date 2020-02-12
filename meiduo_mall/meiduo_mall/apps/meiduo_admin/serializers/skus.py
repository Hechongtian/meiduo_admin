from rest_framework import serializers

from goods.models import SKUImage, SKU, SKUSpecification


class SKUImageSerializer(serializers.ModelSerializer):
    """SKU图片序列化器类"""
    # 关联对象嵌套序列化
    sku = serializers.StringRelatedField(label='SKU商品名称')
    sku_id = serializers.IntegerField(label='SKU商品ID')

    class Meta:
        model = SKUImage
        exclude = ('create_time', 'update_time')

    def validate_sku_id(self, value):
        # sku商品是否存在
        try:
            sku = SKU.objects.get(id=value)
        except SKU.DoesNotExist:
            raise serializers.ValidationError('商品不存在')

        return value

    def create(self, validated_data):
        """sku商品上传图片保存"""
        # 调用ModelSerializer中的create方法
        sku_image = super().create(validated_data)

        # 保存上传图片记录
        sku = SKU.objects.get(id=validated_data['sku_id'])

        # 如果sku商品没有默认图片，则设置其默认图片
        if not sku.default_image:
            sku.default_image = sku_image.image
            sku.save()

        return sku_image

class SKUSimpleSerializer(serializers.ModelSerializer):
    """SKU商品序列化器类"""
    class Meta:
        model = SKU
        fields = ('id', 'name')

class SKUSpecSerializer(serializers.ModelSerializer):
    """商品规格信息序列化器类"""
    spec_id = serializers.IntegerField(label='规格id')
    option_id = serializers.IntegerField(label='选项id')

    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """SKU商品序列化器类"""
    # 关联对象嵌套序列化
    category = serializers.StringRelatedField(label='三级分类名称')

    spu_id = serializers.IntegerField(label='SPU编号')

    # 关联对象嵌套序列化
    specs = SKUSpecSerializer(label='商品规格信息', many=True)

    class Meta:
        model = SKU
        # 排除模型的字段
        exclude = ('create_time', 'update_time', 'default_image', 'spu', 'comments')