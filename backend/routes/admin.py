from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from models.user import User
from models.role import Role
from database import db 

admin_bp = Blueprint('admin', __name__)

def role_required(required_role):
    def wrapper(fn):
        @jwt_required()
        def decorated(*args, **kwargs):
            identity = get_jwt_identity()
            if identity['role'] != required_role:
                return jsonify({"msg": "Access forbidden"}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper

@admin_bp.route('/admin/dashboard', methods=['GET'])
@role_required('Admin')
@jwt_required()
def admin_dashboard():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    role = Role.query.get(user.usr_role)
    
    if role and role.role_name == 'Admin':
        return jsonify({"msg": f"Welcome to the admin dashboard, {user.usr_name}!"}), 200
    else:
        return jsonify({"msg": "Access denied: Admins only"}), 403
    