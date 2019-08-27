from flask import Response, Blueprint, request, jsonify
from app.constants import GET, POST, PUT
from .models import Ingredient, Size, Order, OrderDetail
from .serializers import IngredientSerializer, SizeSerializer, OrderSerializer
from .functions import get_all, calculate_order_price
from .plugins import db
import json

urls = Blueprint('urls', __name__)


# Ingredient Routes

@urls.route('/ingredient', methods=POST)
def create_ingredient():
    ingredient_serializer = IngredientSerializer()
    new_ingredient = ingredient_serializer.load(request.json)
    db.session.add(new_ingredient)
    db.session.commit()
    return Response(json.dumps(request.json), status=201,  mimetype='application/json')


@urls.route('/ingredient', methods=PUT)
def update_ingredient():
    ingredient = Ingredient.query.get(request.json.get('_id'))
    ingredient.name = request.json.get('name') or ingredient.name
    ingredient.price = request.json.get('price') or ingredient.price
    db.session.commit()

    ingredient_serializer = IngredientSerializer()
    return ingredient_serializer.jsonify(ingredient)


@urls.route('/ingredient/id/<_id>', methods=GET)
def get_ingredient_by_id(_id):
    ingredient = Ingredient.query.get(_id)
    ingredient_serializer = IngredientSerializer()
    return ingredient_serializer.jsonify(ingredient)


@urls.route('/ingredient', methods=GET)
def get_ingredients():
    result = get_all(Ingredient, IngredientSerializer)
    return jsonify(result)


# Pizza Size Routes

@urls.route('/size', methods=POST)
def create_size():
    size_serializer = SizeSerializer()
    new_size = size_serializer.load(request.json)
    db.session.add(new_size)
    db.session.commit()
    return Response(json.dumps(request.json), status=201,  mimetype='application/json')


@urls.route('/size', methods=PUT)
def update_size():
    size = Size.query.get(request.json.get('_id'))
    size.name = request.json.get('name') or size.name
    size.price = request.json.get('price') or size.price
    db.session.commit()

    size_serializer = SizeSerializer()
    return size_serializer.jsonify(size)


@urls.route('/size', methods=GET)
def get_sizes():
    result = get_all(Size, SizeSerializer)
    return jsonify(result)


@urls.route('/size/id/<_id>', methods=GET)
def get_size_by_id(_id):
    size = Size.query.get(_id)
    size_serializer = SizeSerializer()
    return size_serializer.jsonify(size)


# Order Routes

@urls.route('/order', methods=POST)
def create_order():
    client_name = request.json.get('client_name')
    client_dni = request.json.get('client_dni')
    client_address = request.json.get('client_address')
    client_phone = request.json.get('client_phone')
    size_id = request.json.get('size_id')
    ingredients = request.json.get('ingredients')

    new_order = Order(client_name=client_name,
                      client_dni=client_dni,
                      client_address=client_address,
                      client_phone=client_phone,
                      size_id=size_id)

    db.session.add(new_order)
    db.session.flush()
    db.session.refresh(new_order)

    db_ingredients = [Ingredient.query.get(ingredient_id) for ingredient_id in ingredients] if isinstance(ingredients, list) else []

    new_order.total_price = calculate_order_price(new_order, db_ingredients)

    db.session.add_all([OrderDetail(order_id=new_order._id,
                                    ingredient_id=ingredient._id,
                                    ingredient_price=ingredient.price)
                        for ingredient in db_ingredients])

    db.session.commit()

    return Response(json.dumps(request.json), status=201,  mimetype='application/json')


@urls.route('/order', methods=GET)
def get_orders():
    result = get_all(Order, OrderSerializer)
    return jsonify(result)


@urls.route('/order/id/<_id>', methods=GET)
def get_order_by_id(_id):
    order = Order.query.get(_id)
    order_serializer = OrderSerializer()
    return order_serializer.jsonify(order)
