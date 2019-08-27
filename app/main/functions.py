
def get_all(Model, Serializer):
    serializer = Serializer(many=True)
    sizes = Model.query.all()
    result = serializer.dump(sizes)
    return result


def calculate_order_price(order, ingredients):

    size_price = order.size.price

    total_ingredient_price = sum(ingredient.price for ingredient in ingredients)

    return size_price + total_ingredient_price
