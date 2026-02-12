from flask import Blueprint, jsonify, request
from services.user_service import UserService
from repositories.user_repository import UserRepository

user_bp = Blueprint("users", __name__, url_prefix="/users")

# instâncias em memória (enquanto app estiver rodando)
_repo = UserRepository()
_service = UserService(_repo)

@user_bp.post("")
def create_user():
    try:
        data = request.get_json(silent=True) or {}
        created = _service.create_user(data)
        return jsonify({"message": "Usuário criado com sucesso.", "user": created}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.get("")
def list_users():
    users = _service.list_users()
    return jsonify({"users": users, "total": len(users)}), 200

@user_bp.get("/<cpf>")
def get_user(cpf: str):
    try:
        user = _service.get_user_by_cpf(cpf)
        return jsonify({"user": user}), 200
    except LookupError as e:
        return jsonify({"error": str(e)}), 404

@user_bp.delete("/<cpf>")
def delete_user(cpf: str):
    try:
        _service.delete_user(cpf)
        return jsonify({"message": "Usuário deletado com sucesso."}), 200
    except LookupError as e:
        return jsonify({"error": str(e)}), 404
