# routes.py
import sqlalchemy
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
    try:
        id = request.json['id']
        if not id.isnumeric():
            return 'ID must be a integer', 400
        username = request.json['username']
        email = request.json['email']
    except:
        return "Id, username, and email are required", 400

    if User.query.get(id):
        return "User already exist with this id", 409
    try:
        user = User(id=id,
                          username=username,
                          email=email)
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return "Username must be unique with the maximum 50 characters, and email must be unique with the maximum 120 characters", 409

    return jsonify(user.serialize)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    user.username = request.json.get('username', user.username)
    user.email = request.json.get('email', user.email)

    try:
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return "Username must be unique with the maximum 50 characters, and email must be unique with the maximum 120 characters", 409

    return jsonify(user.serialize)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return ('', 204)