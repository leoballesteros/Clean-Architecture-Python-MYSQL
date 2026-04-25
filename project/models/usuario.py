from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    id: int | None
    nome: str
    email: str

