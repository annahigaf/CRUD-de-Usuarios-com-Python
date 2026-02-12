from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    nome: str
    email: str
    senha: str
    cpf: str
