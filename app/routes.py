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
        if len(username) > 50:
            return "Username has a maximum 50 of characters", 409

        email = request.json['email']
        if len(email) > 120:
            return "Email has a maximum 120 of characters", 409

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
        return "Username and email must be unique", 409

    return jsonify(user.serialize)



@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    username = request.json.get('username', user.username)
    if len(username) > 50:
        return "Username has a maximum 50 of characters", 409

    email = request.json.get('email', user.email)
    if len(email) > 120:
        return "Email has a maximum 120 of characters", 409

    user.username = username or user.username
    user.email = email or user.email

    try:
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return "Username and email must be unique", 409

    return jsonify(user.serialize)


@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return ('', 204)
