from __future__ import annotations

from typing import Iterable

from project.config.settings import Settings
from project.database.connection import get_connection
from project.database.queries import (
    CREATE_TABLE_USUARIOS,
    DELETE_USUARIO,
    INSERT_USUARIO,
    SELECT_USUARIO_BY_EMAIL,
    SELECT_USUARIO_BY_ID,
    SELECT_USUARIOS,
    UPDATE_USUARIO,
)
from project.models.usuario import Usuario


class UsuarioRepository:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def ensure_schema(self) -> None:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(CREATE_TABLE_USUARIOS)
            connection.commit()

    def create(self, usuario: Usuario) -> Usuario:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(INSERT_USUARIO, (usuario.nome, usuario.email))
            connection.commit()
            usuario_id = int(cursor.lastrowid)
        return Usuario(id=usuario_id, nome=usuario.nome, email=usuario.email)

    def get_by_id(self, usuario_id: int) -> Usuario | None:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_USUARIO_BY_ID, (usuario_id,))
            row = cursor.fetchone()
        if not row:
            return None
        return Usuario(id=int(row[0]), nome=str(row[1]), email=str(row[2]))

    def get_by_email(self, email: str) -> Usuario | None:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_USUARIO_BY_EMAIL, (email,))
            row = cursor.fetchone()
        if not row:
            return None
        return Usuario(id=int(row[0]), nome=str(row[1]), email=str(row[2]))

    def list_all(self) -> list[Usuario]:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_USUARIOS)
            rows: Iterable[tuple[object, object, object]] = cursor.fetchall()
        return [Usuario(id=int(r[0]), nome=str(r[1]), email=str(r[2])) for r in rows]

    def update(self, usuario: Usuario) -> None:
        if usuario.id is None:
            raise ValueError("usuario.id é obrigatório para update")
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(UPDATE_USUARIO, (usuario.nome, usuario.email, usuario.id))
            connection.commit()

    def delete(self, usuario_id: int) -> None:
        with get_connection(self._settings) as connection:
            cursor = connection.cursor()
            cursor.execute(DELETE_USUARIO, (usuario_id,))
            connection.commit()

