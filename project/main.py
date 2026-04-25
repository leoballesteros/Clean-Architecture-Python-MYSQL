from __future__ import annotations

from project.config.settings import load_settings
from project.repositories.usuario_repository import UsuarioRepository
from project.services.usuario_service import UsuarioService


def main() -> None:
    settings = load_settings()

    usuario_repository = UsuarioRepository(settings)
    usuario_repository.ensure_schema()

    usuario_service = UsuarioService(usuario_repository)

    usuarios = usuario_service.listar()
    if not usuarios:
        usuario = usuario_service.cadastrar("Admin", "admin@example.com")
        print(f"Usuário criado: {usuario}")

    print("Usuários:")
    for u in usuario_service.listar():
        print(f"- {u.id}: {u.nome} <{u.email}>")


if __name__ == "__main__":
    main()

