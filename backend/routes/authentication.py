from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify

from models.user import User
from database import db
authentication_bp = Blueprint('authentication', __name__)

@authentication_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('username')   # frontend sends username as "email"
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    user = User.query.filter_by(usr_email=email).first()
    if user and user.check_password(password):
        # Fetch role from Role table
        from models.role import Role
        role = Role.query.get(user.usr_role)

        # Embed both id and role in JWT
        token = create_access_token(identity={
            "id": user.usr_id,
            "role": role.role_name if role else "student"
        })

        return jsonify(access_token=token), 200
    else:
        return jsonify({"msg": "Invalid email or password"}), 401


# #this is only for testing the jwt token, can be removed later    
# @authentication_bp.route('/api/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     identity = get_jwt_identity()   # this is a dict now
#     user = User.query.get(identity["id"])
#     return jsonify(logged_in_as=user.usr_name, role=identity["role"]), 200


@authentication_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role_id = data.get('role_id', 2)  # Default to 'Student' role
    description = data.get('description', '')

    if not username or not email or not password:
        return jsonify({"msg": "Username, email, and password are required"}), 400

    if User.query.filter_by(usr_email=email).first():
        return jsonify({"msg": "Email already exists","email": email}), 400

    new_user = User(usr_name=username, usr_email=email, usr_role=role_id, usr_description=description)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully", "user": new_user.usr_name, "email": new_user.usr_email}), 201

