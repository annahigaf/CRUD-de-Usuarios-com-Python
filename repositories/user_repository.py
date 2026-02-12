from typing import Optional, List, Dict

class UserRepository:
    def __init__(self) -> None:
        self._users: List[Dict[str, str]] = []

    def add(self, user_dict: Dict[str, str]) -> Dict[str, str]:
        self._users.append(user_dict)
        return user_dict

    def list_all(self) -> List[Dict[str, str]]:
        return self._users

    def find_by_cpf(self, cpf: str) -> Optional[Dict[str, str]]:
        for u in self._users:
            if u["cpf"] == cpf:
                return u
        return None

    def delete_by_cpf(self, cpf: str) -> bool:
        for i, u in enumerate(self._users):
            if u["cpf"] == cpf:
                del self._users[i]
                return True
        return False
