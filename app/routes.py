# routes.py
from flask import Blueprint, request, jsonify
from .models import db, User

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([i.serialize for i in users])

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)

    return jsonify(user.serialize)

@users_bp.route('/users', methods=['POST'])
def add_user():
    id = request.json['id']
    username = request.json['username']
    email = request.json['email']
    user = User(id=id,
                      username=username,
                      email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    username = request.json['username']
    email = request.json['email']

    user.username = username
    user.email = email

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return ('', 204)