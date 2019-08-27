from .plugins import ma
from .models import Ingredient, Size, Order


class IngredientSerializer(ma.ModelSchema):

    class Meta:
        model = Ingredient
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.ModelSchema):

    class Meta:
        model = Size
        fields = ('_id', 'name', 'price')


class OrderSerializer(ma.ModelSchema):
    size = ma.Nested(SizeSerializer)
    ingredients = ma.Nested(IngredientSerializer, many=True)

    class Meta:
        model = Order
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'ingredients'
        )
