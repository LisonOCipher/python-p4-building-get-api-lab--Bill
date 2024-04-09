#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    bakery_list = []
    for bakery in bakeries:
        bakery_dict = {
            'id': bakery.id,
            'name': bakery.name,
            'created_at': bakery.created_at  # Include created_at attribute
        }
        bakery_list.append(bakery_dict)
    return jsonify(bakery_list)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get(id)
    bakery_dict = {
        'id': bakery.id,
        'name': bakery.name,
        'created_at': bakery.created_at  # Include created_at attribute
    }
    return jsonify(bakery_dict)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    baked_goods_list = []
    for baked_good in baked_goods:
        baked_good_dict = {
            'id': baked_good.id,
            'name': baked_good.name,
            'price': baked_good.price,
            'created_at': baked_good.created_at,  # Include created_at attribute
            'updated_at': baked_good.updated_at
        }
        baked_goods_list.append(baked_good_dict)
    return jsonify(baked_goods_list)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    baked_good_dict = {
        'id': baked_good.id,
        'name': baked_good.name,
        'price': baked_good.price,
        'created_at': baked_good.created_at,  # Include created_at attribute
        'updated_at': baked_good.updated_at
    }
    return jsonify(baked_good_dict)

if __name__ == '__main__':
    app.run(port=5555, debug=True)