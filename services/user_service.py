from typing import Dict, List
from models.user_model import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def create_user(self, data: Dict) -> Dict[str, str]:
        required = ["nome", "email", "senha", "cpf"]
        missing = [f for f in required if not data.get(f)]
        if missing:
            raise ValueError(f"Campos obrigatórios faltando: {', '.join(missing)}")

        cpf = str(data["cpf"]).strip()

        # regra: não pode CPF repetido
        if self.repo.find_by_cpf(cpf):
            raise ValueError("Já existe usuário com este CPF.")

        user = User(
            nome=str(data["nome"]).strip(),
            email=str(data["email"]).strip(),
            senha=str(data["senha"]).strip(),
            cpf=cpf,
        )

        # repository guarda como dict (requisito)
        return self.repo.add({
            "nome": user.nome,
            "email": user.email,
            "senha": user.senha,
            "cpf": user.cpf
        })

    def list_users(self) -> List[Dict[str, str]]:
        return self.repo.list_all()

    def get_user_by_cpf(self, cpf: str) -> Dict[str, str]:
        user = self.repo.find_by_cpf(str(cpf).strip())
        if not user:
            raise LookupError("Usuário não encontrado.")
        return user

    def delete_user(self, cpf: str) -> None:
        ok = self.repo.delete_by_cpf(str(cpf).strip())
        if not ok:
            raise LookupError("Usuário não encontrado.")
