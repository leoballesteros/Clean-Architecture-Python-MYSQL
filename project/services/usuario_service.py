from __future__ import annotations

from project.models.usuario import Usuario
from project.repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository) -> None:
        self._usuario_repository = usuario_repository

    def cadastrar(self, nome: str, email: str) -> Usuario:
        nome = (nome or "").strip()
        email = (email or "").strip()

        if not nome:
            raise ValueError("nome é obrigatório")
        if "@" not in email or "." not in email:
            raise ValueError("email inválido")

        existente = self._usuario_repository.get_by_email(email)
        if existente is not None:
            raise ValueError("já existe um usuário com esse email")

        return self._usuario_repository.create(Usuario(id=None, nome=nome, email=email))

    def listar(self) -> list[Usuario]:
        return self._usuario_repository.list_all()

